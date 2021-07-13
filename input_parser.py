import meter_telem
import json


class InputParser:
    def __init__(self):

        self.MeterTelem = meter_telem.MeterTelem()
        # self.MeterTelem = self.get_meter_telem_from_input()

    def get_meter_telem_from_input(self, sampling_index):
        # MeterTelem = meter_telem.MeterTelem()

        # Opening JSON file
        f = open('parse.json',)
        # returns JSON object as
        # a dictionary named data
        data = json.load(f)
        # print(data)
        #print(data['Measurements'][sampling_index]['Time'])
        print(data['Measurements'][sampling_index]['Date']+data['Measurements'][sampling_index]['Time'])
        # Closing file
        f.close()

        #assigning new values to
        # MeterTelem from data dictionary
        self.MeterTelem.TimeStamp = data['Measurements'][sampling_index]['Date'] + data['Measurements'][sampling_index]['Time']
        self.MeterTelem.PosEnergy = data['Measurements'][sampling_index]['PosEnergy']
        self.MeterTelem.NegEnergy = data['Measurements'][sampling_index]['NegEnergy']
        self.MeterTelem.PosActivePowerTotal = data['Measurements'][sampling_index]['PosActivePowerTotal']
        self.MeterTelem.NegActivePowerTotal = data['Measurements'][sampling_index]['NegActivePowerTotal']
        self.MeterTelem.CurrentA = data['Measurements'][sampling_index]['CurrentA']
        self.MeterTelem.CurrentB = data['Measurements'][sampling_index]['CurrentB']
        self.MeterTelem.CurrentC = data['Measurements'][sampling_index]['CurrentC']
        self.MeterTelem.VoltageAN = data['Measurements'][sampling_index]['VoltageAN']
        self.MeterTelem.VoltageBN = data['Measurements'][sampling_index]['VoltageBN']
        self.MeterTelem.VoltageCN = data['Measurements'][sampling_index]['VoltageCN']
        self.MeterTelem.Freq = data['Measurements'][sampling_index]['Freq']
        self.MeterTelem.PosActivePowerA = data['Measurements'][sampling_index]['PosActivePowerA']
        self.MeterTelem.PosActivePowerB = data['Measurements'][sampling_index]['PosActivePowerB']
        self.MeterTelem.PosActivePowerC = data['Measurements'][sampling_index]['PosActivePowerC']
        self.MeterTelem.NegActivePowerA = data['Measurements'][sampling_index]['NegActivePowerA']
        self.MeterTelem.NegActivePowerB = data['Measurements'][sampling_index]['NegActivePowerB']
        self.MeterTelem.NegActivePowerC = data['Measurements'][sampling_index]['NegActivePowerC']

        return self.MeterTelem


if __name__ == "__main__":
    input = InputParser()
    input.get_meter_telem_from_input(0)
    print(input.MeterTelem.PosEnergy)








