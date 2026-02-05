team1=input("Enter Home Team: ")
team2=input("Enter Visiting Team: ")
team1_squad=[]
team2_squad=[]
players=int(input("Number of Players per team: "))
i=0
while i<players:
    name=input("Enter the player Name of: ",team1)
    pos=int(input("Enter his batting position: "))
    team1_squad.insert(pos-1,name)
    i=i+1
i=0
while i<players:
    name=input("Enter the player Name of: ",team2)
    pos=int(input("Enter his batting position: "))
    team2_squad.insert(pos,name)
    i=i+1
batting_team_squad=[]
bowling_team_squad=[]
print("---Toss---")
toss_winner=input("Toss Winner: ")
if toss_winner.upper()==team1.upper():
    decision=input("Bat or Bowl First: ")
    if decision.upper()=='BAT':
        batting_team=team1
        batting_team_squad=team1_squad
        bowling_team=team2
        bowling_team_squad=team2_squad
    else:
        batting_team=team2
        batting_team_squad=team2_squad
        bowling_team=team1
        bowling_team_squad=team2_squad
else:
    decision=input("Bat or Bowl First: ")
    if decision.upper()=='BAT':
        batting_team=team2
        bowling_team=team1
    else:
        batting_team=team1
        bowling_team=team2
overs=int(input("Enter Number Of Overs to be played: "))
batting_team_striker=batting_team_squad[0]
batting_team_nonstriker=batting_team_squad[1]
i=0
j=0
batting_order=1
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
                batting_order=batting_order+1
                print("Runs: ",batting_team_runs,"/",wicket)
                print("Batsman: ",batting_team_striker, "Runs: ",batting_team_striker_runs)
                batting_team_striker_runs=0
                if batting_order<players:
                    batting_team_striker=batting_team_squad[batting_order]
                j=j+1
                print("Overs: ",i,".",j)
            else:
                wicket=wicket+1
                batting_order=batting_order+1
                print("Runs: ",batting_team_runs,"/",wicket)
                player_out=input("Who got run-out: (Striker/Non-Striker):")
                if player_out=='Striker':
                    print("Batsman: ",batting_team_striker, "Runs: ",batting_team_striker_runs)
                    batting_team_striker_runs=0
                    if batting_order<players:
                        batting_team_striker=batting_team_squad[batting_order]
                    j=j+1
                    print("Overs: ",i,".",j)
                else:
                    print("Batsman: ",batting_team_nonstriker, "Runs: ",batting_team_nonstriker_runs)
                    batting_team_nonstriker_runs=0
                    if batting_order<players:
                        batting_team_nonstriker=batting_team_squad[batting_order]
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
bowling_team_striker=bowling_team_squad[0]
bowling_team_nonstriker=bowling_team_squad[1]
i=0
j=1
wicket=0
batting_order=1
bowling_team_runs=0
bowling_team_striker_runs=0
bowling_team_nonstriker_runs=0
run_diff=(batting_team_runs+1)-bowling_team_runs
while i<overs and wicket<players and run_diff>0:
    j=0
    while j<6 and wicket<players and run_diff>0:
        run=input("Enter the runs scored: ")
        if run=='1':
            bowling_team_runs=bowling_team_runs+1
            bowling_team_striker_runs=bowling_team_striker_runs+1
            print("Runs: ",bowling_team_runs,"/",wicket)
            print(bowling_team_striker,' :',bowling_team_striker_runs)
            print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
            temp=bowling_team_striker
            bowling_team_striker=bowling_team_nonstriker
            bowling_team_nonstriker=temp
            temp=bowling_team_striker_runs
            bowling_team_striker_runs=bowling_team_nonstriker_runs
            bowling_team_nonstriker_runs=temp
            j=j+1
            print("Overs: ",i,".",j)
            print("Team needs to score: ",run_diff)
        elif run=='2':
            bowling_team_runs=bowling_team_runs+2
            bowling_team_striker_runs=bowling_team_striker_runs+2
            print("Runs: ",bowling_team_runs,"/",wicket)
            print(bowling_team_striker,' :',bowling_team_striker_runs)
            print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
            j=j+1
            print("Overs: ",i,".",j)
            print("Team needs to score ",run_diff)
        elif run=='3':
            bowling_team_runs=bowling_team_runs+3
            bowling_team_striker_runs=bowling_team_striker_runs+3
            print("Runs: ",bowling_team_runs,"/",wicket)
            print(bowling_team_striker,' :',bowling_team_striker_runs)
            print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
            temp=bowling_team_striker
            bowling_team_striker=bowling_team_nonstriker
            bowling_team_nonstriker=temp
            temp=bowling_team_striker_runs
            bowling_team_striker_runs=bowling_team_nonstriker_runs
            bowling_team_nonstriker_runs=temp
            j=j+1
            print("Overs: ",i,".",j)
            print("Team needs to score ",run_diff)
        elif run=='4':
            bowling_team_runs=bowling_team_runs+4
            bowling_team_striker_runs=bowling_team_striker_runs+4
            print("Runs: ",bowling_team_runs,"/",wicket)
            print(bowling_team_striker,' :',bowling_team_striker_runs)
            print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
            j=j+1
            print("Overs: ",i,".",j)
            print("Team needs to score ",run_diff)
        elif run=='5':
            bowling_team_runs=bowling_team_runs+5
            bowling_team_striker_runs=bowling_team_striker_runs+5
            print("Runs: ",bowling_team_runs,"/",wicket)
            print(bowling_team_striker,' :',bowling_team_striker_runs)
            print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
            temp=bowling_team_striker
            bowling_team_striker=bowling_team_nonstriker
            bowling_team_nonstriker=temp
            temp=bowling_team_striker_runs
            bowling_team_striker_runs=bowling_team_nonstriker_runs
            bowling_team_nonstriker_runs=temp
            j=j+1
            print("Overs: ",i,".",j)
            print("Team needs to score ",run_diff)
        elif run=='6':
            bowling_team_runs=bowling_team_runs+4
            bowling_team_striker_runs=bowling_team_striker_runs+4
            print("Runs: ",bowling_team_runs,"/",wicket)
            print(bowling_team_striker,' :',bowling_team_striker_runs)
            print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
            j=j+1
            print("Overs: ",i,".",j)
            print("Team needs to score ",run_diff)
        elif run.upper()=='WICKET':
            mode_wicket=input("Mode of Wicket (Bowled/Caught/Run Out): ")
            if mode_wicket.upper=='BOWLED' or mode_wicket.upper()=='CAUGHT':
                wicket=wicket+1
                batting_order=batting_order+1
                print("Runs: ",bowling_team_runs,"/",wicket)
                print("Batsman: ",bowling_team_striker, "Runs: ",bowling_team_runs)
                bowling_team_striker_runs=0
                if batting_order<players:
                    bowling_team_striker=bowling_team_squad[batting_order]
                j=j+1
                print("Overs: ",i,".",j)
                print("Team needs to score ",run_diff)
            else:
                wicket=wicket+1
                batting_order=batting_order+1
                print("Runs: ",bowling_team_runs,"/",wicket)
                player_out=input("Who got run-out: (Striker/Non-Striker):")
                if player_out=='Striker':
                    print("Batsman: ",bowling_team_striker, "Runs: ",bowling_team_striker_runs)
                    bowling_team_striker_runs=0
                    if batting_order<players:
                        bowling_team_striker=bowling_team_squad[batting_order]
                    j=j+1
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
                else:
                    print("Batsman: ",bowling_team_nonstriker, "Runs: ",bowling_team_nonstriker_runs)
                    bowling_team_nonstriker_runs=0
                    if batting_order<players:
                        bowling_team_nonstriker=bowling_team_squad[batting_order]
                    j=j+1
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
        else:
            mode_extra=input("No Ball/Wide: ")
            if mode_extra=='WIDE':
                bowling_team_runs=bowling_team_runs+1
                print("Runs: ",bowling_team_runs,"/",wicket)
                print("Team needs to score ",run_diff)
            else:
                bowling_team_runs=bowling_team_runs+1
                run=int(input("Extra run Scored:"))
                bowling_team_runs=bowling_team_runs+run
                if run==1:
                    bowling_team_runs=bowling_team_runs+1
                    bowling_team_striker_runs=bowling_team_striker_runs+1
                    print("Runs: ",bowling_team_runs,"/",wicket)
                    print(bowling_team_striker,' :',bowling_team_striker_runs)
                    print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
                    temp=bowling_team_striker
                    bowling_team_striker=bowling_team_nonstriker
                    bowling_team_nonstriker=temp
                    temp=bowling_team_striker_runs
                    bowling_team_striker_runs=bowling_team_nonstriker_runs
                    bowling_team_nonstriker_runs=temp
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
                elif run==2:
                    bowling_team_runs=bowling_team_runs+2
                    bowling_team_striker_runs=bowling_team_striker_runs+2
                    print("Runs: ",bowling_team_runs,"/",wicket)
                    print(bowling_team_striker,' :',bowling_team_striker_runs)
                    print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
                elif run==3:
                    bowling_team_runs=bowling_team_runs+3
                    bowling_team_striker_runs=bowling_team_striker_runs+3
                    print("Runs: ",bowling_team_runs,"/",wicket)
                    print(bowling_team_striker,' :',bowling_team_striker_runs)
                    print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
                    temp=bowling_team_striker
                    bowling_team_striker=bowling_team_nonstriker
                    bowling_team_nonstriker=temp
                    temp=bowling_team_striker_runs
                    bowling_team_striker_runs=bowling_team_nonstriker_runs
                    bowling_team_nonstriker_runs=temp
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
                elif run==4:
                    bowling_team_runs=bowling_team_runs+4
                    bowling_team_striker_runs=bowling_team_striker_runs+4
                    print("Runs: ",bowling_team_runs,"/",wicket)
                    print(bowling_team_striker,' :',bowling_team_striker_runs)
                    print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
                elif run==5:
                    bowling_team_runs=bowling_team_runs+3
                    bowling_team_striker_runs=bowling_team_striker_runs+3
                    print("Runs: ",bowling_team_runs,"/",wicket)
                    print(bowling_team_striker,' :',bowling_team_striker_runs)
                    print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
                    temp=bowling_team_striker
                    bowling_team_striker=bowling_team_nonstriker
                    bowling_team_nonstriker=temp
                    temp=bowling_team_striker_runs
                    bowling_team_striker_runs=bowling_team_nonstriker_runs
                    bowling_team_nonstriker_runs=temp
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
                else:
                    bowling_team_runs=bowling_team_runs+6
                    bowling_team_striker_runs=bowling_team_striker_runs+6
                    print("Runs: ",bowling_team_runs,"/",wicket)
                    print(bowling_team_striker,' :',bowling_team_striker_runs)
                    print(bowling_team_nonstriker,' :',bowling_team_nonstriker_runs)
                    print("Overs: ",i,".",j)
                    print("Team needs to score ",run_diff)
    i=i+1
if run_diff>0:
    print(batting_team," won the match by", run_diff," runs")
elif run_diff==0:
    print("Match Tied")
else:
    print(bowling_team," won the match by", ((players)-(wicket)), "wickets")             
                    



                    









