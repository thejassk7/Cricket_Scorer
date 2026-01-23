team1=input("Enter Home Team: ")
team2=input("Enter Visiting Team: ")
print("---Toss---")
toss_winner=input("Toss Winner: ")
if toss_winner.upper()==team1.upper():
    decision=input("Bat or Bowl First: ")
    if decision.upper()=='BAT':
        batting_team=team1
        bowling_team=team2
    else:
        batting_team=team2
        bowling_team=team1
else:
    decision=input("Bat or Bowl First: ")
    if decision.upper()=='BAT':
        batting_team=team2
        bowling_team=team1
    else:
        batting_team=team1
        bowling_team=team2
overs=int(input("Enter Number Of Overs to be played: "))
players=int(input("Number of Players per team: "))
batting_team_striker=input("Enter Striker: ")
batting_team_nonstriker=input("Enter Non-Striker: ")
i=0
j=1
wicket=0
batting_team_runs=0
batting_team_striker_runs=0
batting_team_nonstriker_runs=0
while i<overs and wicket<players:
    j=0
    while j<6 and wicket<players:
        run=input("Enter the runs scored: ")
        if run=='1':
            batting_team_runs=batting_team_runs+1
            batting_team_striker_runs=batting_team_striker_runs+1
            print("Runs: ",batting_team_runs,"/",wicket)
            print(batting_team_striker,' :',batting_team_striker_runs)
            print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
            temp=batting_team_striker
            batting_team_striker=batting_team_nonstriker
            batting_team_nonstriker=temp
            temp=batting_team_striker_runs
            batting_team_striker_runs=batting_team_nonstriker_runs
            batting_team_nonstriker_runs=temp
            j=j+1
            print("Overs: ",i,".",j)
        elif run=='2':
            batting_team_runs=batting_team_runs+2
            batting_team_striker_runs=batting_team_striker_runs+2
            print("Runs: ",batting_team_runs,"/",wicket)
            print(batting_team_striker,' :',batting_team_striker_runs)
            print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
            j=j+1
            print("Overs: ",i,".",j)
        elif run=='3':
            batting_team_runs=batting_team_runs+3
            batting_team_striker_runs=batting_team_striker_runs+3
            print("Runs: ",batting_team_runs,"/",wicket)
            print(batting_team_striker,' :',batting_team_striker_runs)
            print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
            temp=batting_team_striker
            batting_team_striker=batting_team_nonstriker
            batting_team_nonstriker=temp
            temp=batting_team_striker_runs
            batting_team_striker_runs=batting_team_nonstriker_runs
            batting_team_nonstriker_runs=temp
            j=j+1
            print("Overs: ",i,".",j)
        elif run=='4':
            batting_team_runs=batting_team_runs+4
            batting_team_striker_runs=batting_team_striker_runs+4
            print("Runs: ",batting_team_runs,"/",wicket)
            print(batting_team_striker,' :',batting_team_striker_runs)
            print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
            j=j+1
            print("Overs: ",i,".",j)
        elif run=='5':
            batting_team_runs=batting_team_runs+5
            batting_team_striker_runs=batting_team_striker_runs+5
            print("Runs: ",batting_team_runs,"/",wicket)
            print(batting_team_striker,' :',batting_team_striker_runs)
            print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
            temp=batting_team_striker
            batting_team_striker=batting_team_nonstriker
            batting_team_nonstriker=temp
            temp=batting_team_striker_runs
            batting_team_striker_runs=batting_team_nonstriker_runs
            batting_team_nonstriker_runs=temp
            j=j+1
            print("Overs: ",i,".",j)
        elif run=='6':
            batting_team_runs=batting_team_runs+4
            batting_team_striker_runs=batting_team_striker_runs+4
            print("Runs: ",batting_team_runs,"/",wicket)
            print(batting_team_striker,' :',batting_team_striker_runs)
            print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
            j=j+1
            print("Overs: ",i,".",j)
        elif run.upper()=='WICKET':
            mode_wicket=input("Mode of Wicket (Bowled/Caught/Run Out): ")
            if mode_wicket.upper=='BOWLED' or mode_wicket.upper()=='CAUGHT':
                wicket=wicket+1
                print("Runs: ",batting_team_runs,"/",wicket)
                print("Batsman: ",batting_team_striker, "Runs: ",batting_team_runs)
                batting_team_runs=0
                batting_team_striker=input("Enter New Batsman")
                j=j+1
                print("Overs: ",i,".",j)
            else:
                wicket=wicket+1
                print("Runs: ",batting_team_runs,"/",wicket)
                player_out=input("Who got run-out: (Striker/Non-Striker):")
                if player_out=='Striker':
                    print("Batsman: ",batting_team_striker, "Runs: ",batting_team_striker_runs)
                    batting_team_striker_runs=0
                    batting_team_striker=input("Enter New Batsman")
                    j=j+1
                    print("Overs: ",i,".",j)
                else:
                    print("Batsman: ",batting_team_nonstriker, "Runs: ",batting_team_nonstriker_runs)
                    batting_team_nonstriker_runs=0
                    batting_team_nonstriker=input("Enter New Batsman")
                    j=j+1
                    print("Overs: ",i,".",j)
        else:
            mode_extra=input("No Ball/Wide: ")
            if mode_extra=='WIDE':
                batting_team_runs=batting_team_runs+1
                print("Runs: ",batting_team_runs,"/",wicket)
            else:
                batting_team_runs=batting_team_runs+1
                run=int(input("Extra run Scored:"))
                batting_team_runs=batting_team_runs+run
                if run==1:
                    batting_team_runs=batting_team_runs+1
                    batting_team_striker_runs=batting_team_striker_runs+1
                    print("Runs: ",batting_team_runs,"/",wicket)
                    print(batting_team_striker,' :',batting_team_striker_runs)
                    print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
                    temp=batting_team_striker
                    batting_team_striker=batting_team_nonstriker
                    batting_team_nonstriker=temp
                    temp=batting_team_striker_runs
                    batting_team_striker_runs=batting_team_nonstriker_runs
                    batting_team_nonstriker_runs=temp
                    print("Overs: ",i,".",j)
                elif run==2:
                    batting_team_runs=batting_team_runs+2
                    batting_team_striker_runs=batting_team_striker_runs+2
                    print("Runs: ",batting_team_runs,"/",wicket)
                    print(batting_team_striker,' :',batting_team_striker_runs)
                    print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
                    print("Overs: ",i,".",j)
                elif run==3:
                    batting_team_runs=batting_team_runs+3
                    batting_team_striker_runs=batting_team_striker_runs+3
                    print("Runs: ",batting_team_runs,"/",wicket)
                    print(batting_team_striker,' :',batting_team_striker_runs)
                    print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
                    temp=batting_team_striker
                    batting_team_striker=batting_team_nonstriker
                    batting_team_nonstriker=temp
                    temp=batting_team_striker_runs
                    batting_team_striker_runs=batting_team_nonstriker_runs
                    batting_team_nonstriker_runs=temp
                    print("Overs: ",i,".",j)
                elif run==4:
                    batting_team_runs=batting_team_runs+4
                    batting_team_striker_runs=batting_team_striker_runs+4
                    print("Runs: ",batting_team_runs,"/",wicket)
                    print(batting_team_striker,' :',batting_team_striker_runs)
                    print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
                    print("Overs: ",i,".",j)
                elif run==5:
                    batting_team_runs=batting_team_runs+3
                    batting_team_striker_runs=batting_team_striker_runs+3
                    print("Runs: ",batting_team_runs,"/",wicket)
                    print(batting_team_striker,' :',batting_team_striker_runs)
                    print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
                    temp=batting_team_striker
                    batting_team_striker=batting_team_nonstriker
                    batting_team_nonstriker=temp
                    temp=batting_team_striker_runs
                    batting_team_striker_runs=batting_team_nonstriker_runs
                    batting_team_nonstriker_runs=temp
                    print("Overs: ",i,".",j)
                else:
                    batting_team_runs=batting_team_runs+6
                    batting_team_striker_runs=batting_team_striker_runs+6
                    print("Runs: ",batting_team_runs,"/",wicket)
                    print(batting_team_striker,' :',batting_team_striker_runs)
                    print(batting_team_nonstriker,' :',batting_team_nonstriker_runs)
                    print("Overs: ",i,".",j)
    i=i+1            
                   
                    



                    









