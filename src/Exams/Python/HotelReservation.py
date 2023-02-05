class Passenger:
    def __init__(self, name, city, rooms):
        if not isinstance(name, str) or not isinstance(city, str) or not isinstance(rooms, dict):
            raise self.PassengerError('Invalid type')
        self.__name = name
        self.__city = city
        self.__rooms = rooms

    def __repr__(self):
        return 'Passenger name: {}, city: {}, rooms: {}'.format(self.__name, self.__city, self.__rooms)

    class PassengerError(Exception):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise self.PassengerError('Invalid city')
        self.__city = city

    @property
    def rooms(self):
        return self.__rooms


class Hotel:
    def __init__(self, city, rooms):
        if not isinstance(city, str) or not isinstance(rooms, dict):
            raise self.HotelError('Invalid type')
        self.__city = city
        self.__rooms = rooms

    def __repr__(self):
        return 'Hotel in city: {}, rooms: {}'.format(self.__city, self.__rooms)

    class HotelError(Exception):
        pass

    @property
    def city(self):
        return self.__city

    @property
    def rooms(self):
        return self.__rooms

    def get_city(self):
        return self.city

    def free_rooms_list(self, room):
        if room in self.rooms:
            return self.rooms[room]
        else:
            raise self.HotelError('There is no such room')

    def reserve_rooms(self, room, count):
        if self.free_rooms_list(room) >= count:
            self.rooms[room] -= count
            return True
        else:
            print('Not enough free rooms of type {}'.format(room))
            return False


def book(passenger, hotel, room, count):
    if passenger.city == hotel.city and hotel.reserve_rooms(room, count):
        if room in passenger.rooms:
            passenger.rooms[room] += count
        else:
            passenger.rooms[room] = count
        print('Reservation successful!')
        return True
    else:
        print('Reservation failed. Please try again.')
        return False


# Testing all functions
passenger = Passenger('Artur Karapetyan', 'Yerevan', {'Single': 2})
hotel = Hotel('Yerevan', {'Single': 14, 'Double': 7, 'Penthouse': 3})
print(passenger)
print(hotel)
print(hotel.free_rooms_list('Single'))
book(passenger, hotel, 'Double', 2)
print(hotel.free_rooms_list('Single'))
print(hotel)
print(passenger)
