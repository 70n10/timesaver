import requests

def matches(link):
    def computeScore(x):
        resh, resa = 0, 0
        for i in range(1, len(data[x]["setResults"]) + 1):
            if data[x]["setResults"]["{}".format(i)]["home"] > data[x]["setResults"]["{}".format(i)]["away"]:
                resh += 1
            else:
                resa += 1

        return (str(resh) + '-' + str(resa))
    response = requests.get(link)
    data = response.json()
    toreturn = ''
    for team in range(0, len(data)+1):
        try:
            toreturn += (data[team]["teams"]["home"]["caption"].replace('VBC', '').replace('VB', '').replace('Volley', '').strip() + ' - '
                  + data[team]["teams"]["away"]["caption"].replace('VBC', '').replace('VB', '').replace('Volley', '').strip()
                  +'\t' + computeScore(team)) + '<br>'
        except:
            pass
    return toreturn


def classement(link):
    response_ranking = requests.get(link)
    data_ranking = response_ranking.json()
    toreturn = ''
    for i in range(len(data_ranking)-1):
        toreturn+=(str(i+1) +'.'+ '\t' + data_ranking[i]['teamCaption'].replace('VBC', '').replace('VB', '').replace('Volley', '').strip()
              + '\t' + str(data_ranking[i]['games'])
              + '\t' + str(data_ranking[i]['winsClear'])
              + '\t' + str(data_ranking[i]['winsNarrow'])
              + '\t' + str(data_ranking[i]['defeatsClear'])
              + '\t' + str(data_ranking[i]['defeatsNarrow'])
              + '\t' + str(data_ranking[i]['setsWon'])
              + '-' +  str(data_ranking[i]['setsLost'])
              + '\t' + str(data_ranking[i]['points']) + '<br>'
              )
    return toreturn