import requests # type: ignore
import openpyxl # type: ignore

def buscar_personagens():
    url = "http://localhost:8080/character"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()

def criar_excel_personagens():
    personagens = buscar_personagens()

    wb = openpyxl.Workbook()
    planilha = wb.active

    planilha.append(["ID", "Nome", "Nome Real", "Idade"])

    for personagem in personagens:
        planilha.append([personagem["id"], personagem["name"], personagem["realName"], personagem["age"]])

    wb.save("personagens.xlsx")

if __name__ == "__main__":
    criar_excel_personagens()
