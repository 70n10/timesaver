import foot
import volley
import time

groupe = {'Deuxième ligue <br>' : 'https://www.football.ch/anf/Association-neuchateloise-de-football/Competition-ANF/Championnat-ANF.aspx/oid-15/s-2019/ln-13010/',
          'Troisième ligue, groupe 1 <br>':'https://www.football.ch/anf/Association-neuchateloise-de-football/Competition-ANF/Championnat-ANF.aspx/oid-15/s-2019/ln-13020/ls-17480/sg-51496/a-mrr/',
          'Groupe 2 <br>':'https://www.football.ch/anf/Association-neuchateloise-de-football/Competition-ANF/Championnat-ANF.aspx/oid-15/s-2019/ln-13020/ls-17480/sg-51497/a-mrr/',
          'Quatrième ligue, groupe 1 <br>' : 'https://www.football.ch/anf/Association-neuchateloise-de-football/Competition-ANF/Championnat-ANF.aspx/oid-15/s-2019/ln-13030/ls-17481/sg-51498/a-mrr/',
          'Groupe 2 <br>':'https://www.football.ch/anf/Association-neuchateloise-de-football/Competition-ANF/Championnat-ANF.aspx/oid-15/s-2019/ln-13030/ls-17481/sg-51499/a-mrr/',
          'Groupe 3 <br>':'https://www.football.ch/anf/Association-neuchateloise-de-football/Competition-ANF/Championnat-ANF.aspx/oid-15/s-2019/ln-13030/ls-17481/sg-51500/a-mrr/',
          'Cinquième ligue <br>':'https://www.football.ch/anf/Association-neuchateloise-de-football/Competition-ANF/Championnat-ANF.aspx/oid-15/s-2019/ln-13040/'}
toprint = ''
def contentfoot():
    toprint = str(time.asctime()) + '<br>'
    for j,i in groupe.items():
        toprint += j
        toprint += foot.matches(i)
        toprint += foot.classement(i)
    return(toprint)

def contentvolley():
    toprint = str(time.asctime()) + '<br>'
    toprint += volley.matches("https://api.volleyball.ch/indoor/games?region=SV&gender=f&leagueId=1973&phaseId=3482&groupId=11778")
    toprint += volley.classement("https://api.volleyball.ch/indoor/ranking/11778")
    return toprint