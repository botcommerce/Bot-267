from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class MyJSONElement:
    height: int
    id: int
    ikpu_code: int
    in_stock: bool
    length: int
    name: str
    package_code: int
    price: str
    weight: int
    width: int

    def __init__(self, height: int, id: int, ikpu_code: int, in_stock: bool, length: int, name: str, package_code: int,
                 price: str, weight: int, width: int) -> None:
        self.height = height
        self.id = id
        self.ikpu_code = ikpu_code
        self.in_stock = in_stock
        self.length = length
        self.name = name
        self.package_code = package_code
        self.price = price
        self.weight = weight
        self.width = width

    @staticmethod
    def from_dict(obj: Any) -> 'MyJSONElement':
        assert isinstance(obj, dict)
        height = from_int(obj.get("height"))
        id = from_int(obj.get("id"))
        ikpu_code = from_int(obj.get("ikpu_code"))
        in_stock = from_bool(obj.get("in_stock"))
        length = from_int(obj.get("length"))
        name = from_str(obj.get("name"))
        package_code = from_int(obj.get("package_code"))
        price = from_str(obj.get("price"))
        weight = from_int(obj.get("weight"))
        width = from_int(obj.get("width"))
        return MyJSONElement(height, id, ikpu_code, in_stock, length, name, package_code, price, weight, width)

    def to_dict(self) -> dict:
        result: dict = {"height": from_int(self.height), "id": from_int(self.id), "ikpu_code": from_int(self.ikpu_code),
                        "in_stock": from_bool(self.in_stock), "length": from_int(self.length),
                        "name": from_str(self.name), "package_code": from_int(self.package_code),
                        "price": from_str(self.price), "weight": from_int(self.weight), "width": from_int(self.width)}
        return result


def my_json_from_dict(s: Any) -> List[MyJSONElement]:
    return from_list(MyJSONElement.from_dict, s)


def my_json_to_dict(x: List[MyJSONElement]) -> dict:
    my_dict = {}
    for element in x:
        my_dict[element.id] = element.to_dict()
    return my_dict


def sort_dict_by_id_asc(my_dict: dict) -> dict:
    return {k: v for k, v in sorted(my_dict.items(), key=lambda x: x[1]["id"])}


my_json_list = [
    MyJSONElement(10, 6, 123, True, 20, "Product 1", 456, "9.99", 100, 30),
    MyJSONElement(15, 1, 456, False, 25, "Product 2", 789, "19.99", 200, 40),
    MyJSONElement(8, 3, 789, True, 15, "Product 3", 123, "29.99", 300, 50)
]

my_json_dict = my_json_to_dict(my_json_list)
sorted_dict = sort_dict_by_id_asc(my_json_dict)

print(my_json_dict)
print(sorted_dict)
