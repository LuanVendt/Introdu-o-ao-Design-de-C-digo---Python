from flask import request as Flaskrequest
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler


class Calculator2:
    def calculate(self, request: Flaskrequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)

        formated_response = self.__format_response(calculated_number)

        return formated_response

    @staticmethod
    def __validate_body(body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    @staticmethod
    def __process_data(input_data: List[float]) -> float:
        numpy_handler = NumpyHandler()
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = numpy_handler.standard_derivation(first_process_result)

        return 1/result

    @staticmethod
    def __format_response(calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }
