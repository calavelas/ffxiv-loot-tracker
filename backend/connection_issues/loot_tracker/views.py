from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Character, Patch, StaticLootHistory, StaticMember, StaticBIS

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Index(APIView):
    def get(self, request):

        # RaidMembers = StaticMember.objects.all()
        RaidMembers = StaticMember.objects.filter(static__name="Connection Issues")


        #Get RaidMember
        RaidMembersList = []
        for member in RaidMembers:
            RaidMembersList.append(
                {
                "Id" : member.id,
                "Name" : member.getName(),
                "Job" : member.getJob(),
                "Role" : member.getRole(),
                "Bis" : {},
                "Loot" : []
                }
            )
        for member in RaidMembersList:


            #Get BIS Data
            memberBisQuerySet = StaticBIS.objects.filter(character__id=member['Id']).order_by('item__type')
            for query in memberBisQuerySet:
                member['Bis'][query.item.type] = {
                        "Name" : query.item.name,
                        "isRaid" : query.item.isRaid,
                        "iLevel" : query.item.iLevel,
                        "xivApiId" : query.item.xivApiId
                    }

            #Get BIS Data
            memberLootHistoryQuerySet = StaticLootHistory.objects.filter(character__id=member['Id']).order_by('-timestamp')
            print(memberLootHistoryQuerySet)
            for query in memberLootHistoryQuerySet:
                member["Loot"].append(
                    {
                        "Id" : query.item.id,
                        "Name" : query.item.name,
                        "Timestamp" : query.timestamp
                    }
                )



        result = {
            "RaidMembers" : RaidMembersList,
            "Total" : len(RaidMembersList)
        }
        return Response(result)

class CheckItem(APIView):
    def get(self, request):

        #Query Parameter
        staticName = self.request.query_params.get('staticName')
        itemName = self.request.query_params.get('itemName')

        #Query Data from Database
        staticMemberQuerySet = StaticMember.objects.filter(static__name=staticName)
        staticLootHistoryQuerySet = StaticLootHistory.objects.filter(item__name=itemName).order_by("-timestamp")

        #Setup Variable for Static Member
        staticMembers = set()
        totalMemberLoot = {}

        for query in staticMemberQuerySet:
            staticMembers.add(query.character.name)
            totalMemberLoot[query.character.name] = staticLootHistoryQuerySet.filter(member__character__name=query.character.name).count()


        cycleCount = 1
        currentCycle = set()
        nextCycle = set()
        nextNextCycle = set()
        lootHistoryList = []

        for query in staticLootHistoryQuerySet:
            if query.member.character.name in (currentCycle and nextCycle):
                nextNextCycle.add(query.member.character.name)
                print(f"Add {query.member.character.name} to nextNextCycle")
            elif query.member.character.name in currentCycle:
                nextCycle.add(query.member.character.name)
                print(f"Add {query.member.character.name} to nextCycle")
            elif query.member.character.name not in currentCycle:
                currentCycle.add(query.member.character.name)
                print(f"Add {query.member.character.name} to currentCycle")
            print(currentCycle)
            print(nextCycle)
            lootHistoryList.append(
                    {
                        "transactionId" : query.id,
                        "takenBy" : query.member.character.name,
                        "itemId" : query.item.id,
                        "Name" : query.item.name,
                        "Timestamp" : query.timestamp
                    }
                )
        #Resetting Cycle
            if currentCycle == staticMembers:
                if len(nextCycle) != 0:
                    currentCycle = nextCycle
                    nextCycle = nextNextCycle
                    nextNextCycle = set()
                    cycleCount += 1
                    leftover = staticMembers-currentCycle
                    print("new cycle copy 2 to 1")
                else:
                    currentCycle = nextCycle
                    nextCycle = set()
                    cycleCount += 1
                    leftover = staticMembers-currentCycle
                    print("new cycle start over")
            else:
                leftover = staticMembers-currentCycle

        result = {
            "StaticName" : staticName,
            "ItemName" : itemName,
            "staticMember" : staticMembers,
            "cycle" : cycleCount,
            "currentCycle" : currentCycle,
            "nextCycle" : nextCycle,
            "nextNextCycle" : nextNextCycle,
            "waitingLine" : leftover,
            "lootHistory" : lootHistoryList,
            "statistic" : {
                "totalLoot" : staticLootHistoryQuerySet.count(),
                "totalMemberLoot" : totalMemberLoot
            }
        }
        return Response(result)

class CharacterView(APIView):
    def get(self, request, name):
        characterQuery = Character.objects.filter(first_name=name)

        result = []
        for item in characterQuery:
            result.append(
                {
                "Name" : item.first_name
                }
            )

        return Response(result)

class TestIndex(APIView):
    def get(self, request):

        Static = StaticMember.objects.all()
        member_list = []
        for member in Static:
            member_list.append(
                {
                "Name" : member.getName(),
                "Job" : member.getJob(),
                "Role" : member.getRole()
                }
            )

        return Response(member_list)

class Bis(APIView):
    def get(self, request):

        # RaidMembers = StaticMember.objects.all()
        RaidMembers = StaticMember.objects.filter(static__name="Connection Issues")
        RaidMembersList = []
        for member in RaidMembers:
            RaidMembersList.append(
                {
                "Id" : member.id,
                "Name" : member.getName(),
                "Job" : member.getJob(),
                "Role" : member.getRole(),
                "Bis" : {}
                }
            )
        for member in RaidMembersList:
            memberItemQuerySet = StaticBIS.objects.filter(character__id=member['Id']).order_by('item__type')

            for item in memberItemQuerySet:
                member['Bis'][item.item.type] = {
                        "Name" : item.item.name,
                        "isRaid" : item.item.isRaid,
                        "iLevel" : item.item.iLevel,
                        "xivApiId" : item.item.xivApiId
                    }

        result = {
            "RaidMembers" : RaidMembersList,
            "Total" : len(RaidMembersList)
        }
        return Response(result)








def brd(request):
    brd = Character.objects.filter(job__name="Bard")
    return HttpResponse(brd)

def blm(request):
    blm = Character.objects.filter(job__name="Black Mage")
    return HttpResponse(blm)

def bis(request):
    bis_table = StaticBIS.objects.filter(character__static__name="Connection Issues")
    raid_bis = []

    for row in bis_table:
        if row.item.isRaid == True:
            raid_bis.append(
            {
            "Name" : row.character.getName(),
            "Item" : row.item.name,
            "Job" : row.character.getJob(),
            "Role" : row.character.getRole(),
            "Patch" : row.patch.number
            }
        )

    result = {
        "result" : raid_bis
    }

    return JsonResponse(result)
