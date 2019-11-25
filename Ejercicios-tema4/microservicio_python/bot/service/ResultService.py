from bot.model.Result import Result
import requests
from bs4 import BeautifulSoup

class ResultService():

    @staticmethod
    def addResult(local, visit, rlocal, rvisit):
        try:
            result = Result()
            result.setTeamLocal(local)
            result.setTeamVisit(visit)
            result.setResultLocal(rlocal)
            result.setResultVisit(rvisit)
            result.save()
            return True
        except:
            return False

    @staticmethod
    def getResult(id):

        try:
            result = Result.get(Result.id == id)
        except:
            return None
        return result

    @staticmethod
    def getResultByLocal(local):

        try:
            result = Result.get(Result.teamLocal == local)
        except:
            return None
        return result

    @staticmethod
    def getResultByVisit(visit):

        try:
            result = Result.get(Result.teamVisit == visit)
        except:
            return None
        return result

    @staticmethod
    def getAll():

        try:
            listResults =[]
            result = Result.select()
            for r in result:
                listResults.append(r)
            result = listResults
        except:
            return None
        return result

    @staticmethod
    def getResultLocal(id):
        try:
            result = Result.get(Result.id == id)
        except:
            return None
        return result.getResultLocal()

    @staticmethod
    def inserDataResult():
        """Funcion que scrapea de la web la información de los resultados de la jornada de la liga española de fútbol.
        """
        url = "http://resultados.as.com/resultados/futbol/primera/jornada/"

        req = requests.get(url)

        v_tlocal = []  # vector equipos locales
        v_tvisit = []  # vector equipos visitantes
        v_result = []  # vector resultados
        v_result_local = []
        v_result_visit = []
        v_fecha = []  # vecto fechas

        statusCode = req.status_code
        if statusCode == 200:

            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text, "html.parser")

            # Obtenemos todos los divs donde estan las entradas de los equipos locales
            entradas = html.find_all('div', {'class': 'equipo-local'})
            for i, entrada in enumerate(entradas):
                equipo_local = entrada.find('span', {'class': 'nombre-equipo'}).getText()
                v_tlocal.insert(i, equipo_local)

            # Obtenemos todos los divs donde estan las entradas de los equipos visitantes
            entradas2 = html.find_all('div', {'class': 'equipo-visitante'})
            for i, entrada in enumerate(entradas2):
                equipo_visit = entrada.find('span', {'class': 'nombre-equipo'}).getText()
                v_tvisit.insert(i, equipo_visit)

            # Obtenemos todos los divs donde estan los resultados finalizados
            entradas3 = html.find_all('a', {'class': 'resultado'})
            for i, entrada in enumerate(entradas3):
                # resultado = entrada.find('a', {'class' : 'resultado'}).getText()
                v_result.insert(i, entrada.text)
                print(entrada.text)
                result = entrada.text
                position = result.find('-')
                v_result_local.insert(i, int(""+result[position-2]))
                v_result_visit.insert(i, int(""+result[position + 2]))

            if len(v_result) < 10:
                for i in range(len(v_result), 10):
                    v_result.insert(i, "-")

            # Obtenemos todos los divs donde estan las fechas
            entradas4 = html.find_all('span', {'class': 'fecha'})
            for i, entrada in enumerate(entradas4):
                # resultado = entrada.find('a', {'class' : 'resultado'}).getText()
                v_fecha.insert(i, entrada.text)

            # print (entradas)

            for i in range(10):
                # fun_bd.insertResultados(v_tlocal[i], v_result[i], v_tvisit[i], i + 1)
                try:
                    result = Result.select().where(Result.id == i).get()
                    result.setTeamLocal(v_tlocal[i])
                    result.setTeamVisit(v_tvisit[i])
                    result.setResultLocal(int(v_result_local[i]))
                    result.setResultVisit(int(v_result_visit[i]))
                    result.save()
                except:
                    result = Result()
                    result.setTeamLocal(v_tlocal[i])
                    result.setTeamVisit(v_tvisit[i])
                    result.setResultLocal(int(v_result_local[i]))
                    result.setResultVisit(int(v_result_visit[i]))
                    result.save()

        else:
            print ("Status Code %d" % statusCode)
