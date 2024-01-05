import json
from seleniumbase import BaseCase

matsum = []

class MatchSummary(BaseCase):
    
    def test_summary(self):
        self.open('https://www.espncricinfo.com/records/tournament/team-match-results/icc-cricket-world-cup-2023-24-15338')
        
        for i in range(1, 49):        
            team1 = self.get_text_content(f'/html/body/div/section/section/div[4]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[{1}]', by='xpath')
            team2 = self.get_text_content(f'/html/body/div/section/section/div[4]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[{2}]', by='xpath')
            winner = self.get_text_content(f'/html/body/div/section/section/div[4]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[{3}]', by='xpath')
            margin = self.get_text_content(f'/html/body/div/section/section/div[4]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[{4}]', by='xpath')
            ground = self.get_text_content(f'/html/body/div/section/section/div[4]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[{5}]', by='xpath')
            matchDate = self.get_text_content(f'/html/body/div/section/section/div[4]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[{6}]', by='xpath')
            scorecard = self.get_text_content(f'/html/body/div/section/section/div[4]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[{7}]', by='xpath')

            match = {
                "team1": team1,
                "team2": team2,
                "winner": winner,
                "margin": margin,
                "ground": ground,
                "matchDate": matchDate,
                "scorecard": scorecard
            }
            print(match)
            matsum.append(match)

        res = [{"matchSummary": matsum}]

        with open('match_results3.json', 'w') as file:
            json.dump(res, file)

