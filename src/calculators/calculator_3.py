from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)

        formated_response = self.__format_response(multiplication)

        return formated_response

    @staticmethod
    def __validate_body(body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)

        return variance

    @staticmethod
    def __calculate_multiplication(numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num

        return multiplication

    @staticmethod
    def __verify_results(variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Falha no processo: Variância menor que multiplicação!")

    @staticmethod
    def __format_response(variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "Success": True
            }
        }
