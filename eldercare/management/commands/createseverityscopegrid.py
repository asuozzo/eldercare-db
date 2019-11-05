from django.core.management.base import BaseCommand
from eldercare.models import Severity_Scope

class Command(BaseCommand):

    def handle(self, *args, **options):
        for letter in severity_scope:
            try:
                ss = Severity_Scope.objects.create(
                    letter=letter[0],
                    score=letter[1],
                    severity=letter[2],
                    severity_code=letter[3],
                    scope=letter[4],
                    scope_code=letter[5]
                )
                
            except Exception as e:
                print("failed on {0} {1}".format(row["Letter"]))


severity_scope = [
    ["A",0,"No actual harm with potential for minor negative impact",1,"Isolated",1],
    ["B",0,"No actual harm with potential for minor negative impact",1,"Pattern",2],
    ["C",0,"No actual harm with potential for minor negative impact",1,"Widespread",3],
    ["D",4,"No actual harm with potential for more than minimal harm, or actual minimal harm (discomfort)",2,"Isolated",1],
    ["E",8,"No actual harm with potential for more than minimal harm, or actual minimal harm (discomfort)",2,"Pattern",2],
    ["F",16,"No actual harm with potential for more than minimal harm, or actual minimal harm (discomfort)",2,"Widespread",3],
    ["G",20,"Actual harm that is not immediate jeopardy",3,"Isolated",1],
    ["H",35,"Actual harm that is not immediate jeopardy",3,"Pattern",2],
    ["I",45,"Actual harm that is not immediate jeopardy",3,"Widespread",3],
    ["J",50,"Immediate jeopardy to resident health or safety",4,"Isolated",1],
    ["K",100,"Immediate jeopardy to resident health or safety",4,"Pattern",2],
    ["L",150,"Immediate jeopardy to resident health or safety",4,"Widespread",3]
]