import unittest
import requests
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService
db.init('dercn75nklk4a6', host='ec2-54-246-92-116.eu-west-1.compute.amazonaws.com', user='awolxnvarfbuje', password='50af008532aaf685ecf1e4bc9d397528354600f3de0a41554cf8291284b0eb93')


class ResultTest(unittest.TestCase):

    def test_check_result_by_id(self):
        """
        Test que comprueba la búsqueda de un resultados por su id
        :return:
        """
        result = True

        if(rService.getResult(1) is None):
            result = False

        self.assertTrue(result)

    def test_check_result_by_name(self):
        """
                Test que comprueba la búsqueda de un resultado por su nombre de equipo local o visitante
                :return:
                """
        result = False

        if (rService.getResultByLocal("Valencia") is not None):
            result = True
        elif (rService.getResultByVisit("Valencia") is not None):
            result = True

        self.assertTrue(result)

    def test_check_all_results(self):
        """
        Test que comprueba la búsqueda de todos los resultados
        :return:
        """
        result = True

        if (rService.getAll() is None):
            result = False

        self.assertTrue(result)

    def test_check_local_score_result(self):
        """
        Test que comprueba la búsqueda del marcador local de un partido
        :return:
        """
        result = True

        if (rService.getResultLocal(1) is None):
            result = False

        self.assertTrue(result)

    def test_name_team(self):
        """
        Test que comprueba que el nombre del equipo buscado es el devuelto
        :return:
        """
        result = Result()
        name = ""
        team = "Valencia"
        if (rService.getResultByLocal("Valencia") is not None):
            result = rService.getResultByLocal("Valencia")
            name = result.getTeamLocal()
        elif (rService.getResultByVisit("Valencia") is not None):
            result = rService.getResultByVisit("Valencia")
            name = result.getTeamVisit()

        self.assertEqual(name, team)

if __name__ == '__main__':
   unittest.main()