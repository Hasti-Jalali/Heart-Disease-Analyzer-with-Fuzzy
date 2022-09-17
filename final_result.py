import inference
import defuzzification
class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        inference_result = inference.inference(input_dict)
        def_string = defuzzification.defuzzification(inference_result)
        print(def_string)
        return def_string

