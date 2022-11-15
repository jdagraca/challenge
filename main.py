from dotenv import load_dotenv
from src.porcesarpagos import ProcesarPagos

load_dotenv()


if __name__ == "__main__":
    print("Inicio de proceso")

    ProcesarPagos.run()
