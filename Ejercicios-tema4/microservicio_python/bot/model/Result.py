from peewee import *
from bot.model.BaseModel import BaseModel


class Result(BaseModel):
    id = AutoField(primary_key=True)
    teamLocal = CharField(max_length=50, null=False)
    teamVisit = CharField(max_length=50, null=False)
    resultLocal = IntegerField(null=True)
    resultVisit = IntegerField(null=True)

    def getId(self):
        return self.id

    def getTeamLocal(self):
        return self.teamLocal

    def setTeamLocal(self, teamLocal):
        self.teamLocal = teamLocal

    def getTeamVisit(self):
        return self.teamVisit

    def setTeamVisit(self, teamVisit):
        self.teamVisit = teamVisit

    def getResultLocal(self):
        return self.resultLocal

    def setResultLocal(self, resultLocal):
        self.resultLocal = resultLocal

    def getResultVisit(self):
        return self.resultVisit

    def setResultVisit(self, resultVisit):
        self.resultVisit = resultVisit

