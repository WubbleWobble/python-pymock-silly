from Thing.api import Api
from Thing.thing import Thing

def test_thing(mocker):
    mocker.patch(
        'Thing.api.Api.stats',
        return_value=[1,2,3,4,5]
    )

    api = Api('https://www.example.org/thing')
    thing = Thing(api)

    expected = 15
    actual = thing.total()

    assert expected == actual