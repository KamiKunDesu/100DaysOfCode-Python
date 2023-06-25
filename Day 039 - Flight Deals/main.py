from FlightPathManager import flight_path_database_command, flight_path_database_query, flight_path

lon_tko = flight_path.FlightPath('London', 'Tokyo', 0, '', '')
flight_path_datatbase_command = flight_path_database_command.FlightPathDatabaseCommand()
flight_path_datatbase_query = flight_path_database_query.FlightPathDatabaseQuery()

flight_path_datatbase_command.add_flight_path(lon_tko)

