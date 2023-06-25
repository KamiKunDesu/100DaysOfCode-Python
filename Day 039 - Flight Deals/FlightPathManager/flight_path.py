class FlightPath:
    '''This class will be used to create flight paths for the SQL database. It will include a start
    destination, a return destination (setting up a route pair) and a historic low cost, as well as an
    AITA code for both the start and end destination'''

    def __init__(self, start_destination: str, end_destination: str, historic_low_cost: int, start_destination_aita_code: str, end_destination_aita_code: str) -> None:
        '''This function will initialise the class and store the start destination, end destination, historic low cost, 
        start destination AITA code and end destination AITA code'''
        self.start_destination: str = start_destination
        self.end_destination: str = end_destination
        self.historic_low_cost: int = historic_low_cost
        self.start_destination_aita_code: str = start_destination_aita_code
        self.end_destination_aita_code: str = end_destination_aita_code

    def start_destination_get(self) -> str:
        '''This function will return the start destination'''
        return self.start_destination
    
    def end_destination_get(self) -> str:
        '''This function will return the end destination'''
        return self.end_destination
    
    def historic_low_cost_get(self) -> int:
        '''This function will return the historic low cost'''
        return self.historic_low_cost
    
    def start_destination_aita_code_get(self) -> str:
        '''This function will return the start destination AITA code'''
        return self.start_destination_aita_code
    
    def end_destination_aita_code_get(self) -> str:
        '''This function will return the end destination AITA code'''
        return self.end_destination_aita_code
    
    