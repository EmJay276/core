"""Make sure that Eve Degree (via Eve Extend) is enumerated properly."""

from homeassistant.components.number import NumberMode
from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import PERCENTAGE, PRESSURE_HPA, TEMP_CELSIUS
from homeassistant.helpers.entity import EntityCategory

from ..common import (
    HUB_TEST_ACCESSORY_ID,
    DeviceTestInfo,
    EntityTestInfo,
    assert_devices_and_entities_created,
    setup_accessories_from_file,
    setup_test_accessories,
)


async def test_eve_degree_setup(hass):
    """Test that the accessory can be correctly setup in HA."""
    accessories = await setup_accessories_from_file(hass, "eve_degree.json")
    await setup_test_accessories(hass, accessories)

    await assert_devices_and_entities_created(
        hass,
        DeviceTestInfo(
            unique_id=HUB_TEST_ACCESSORY_ID,
            name="Eve Degree AA11",
            model="Eve Degree 00AAA0000",
            manufacturer="Elgato",
            sw_version="1.2.8",
            hw_version="1.0.0",
            serial_number="AA00A0A00000",
            devices=[],
            entities=[
                EntityTestInfo(
                    entity_id="sensor.eve_degree_aa11_temperature",
                    unique_id="homekit-AA00A0A00000-22",
                    friendly_name="Eve Degree AA11 Temperature",
                    capabilities={"state_class": SensorStateClass.MEASUREMENT},
                    unit_of_measurement=TEMP_CELSIUS,
                    state="22.7719116210938",
                ),
                EntityTestInfo(
                    entity_id="sensor.eve_degree_aa11_humidity",
                    unique_id="homekit-AA00A0A00000-27",
                    friendly_name="Eve Degree AA11 Humidity",
                    capabilities={"state_class": SensorStateClass.MEASUREMENT},
                    unit_of_measurement=PERCENTAGE,
                    state="59.4818115234375",
                ),
                EntityTestInfo(
                    entity_id="sensor.eve_degree_aa11_air_pressure",
                    unique_id="homekit-AA00A0A00000-aid:1-sid:30-cid:32",
                    friendly_name="Eve Degree AA11 Air Pressure",
                    unit_of_measurement=PRESSURE_HPA,
                    capabilities={"state_class": SensorStateClass.MEASUREMENT},
                    state="1005.70001220703",
                ),
                EntityTestInfo(
                    entity_id="sensor.eve_degree_aa11_battery",
                    unique_id="homekit-AA00A0A00000-17",
                    friendly_name="Eve Degree AA11 Battery",
                    capabilities={"state_class": SensorStateClass.MEASUREMENT},
                    unit_of_measurement=PERCENTAGE,
                    state="65",
                ),
                EntityTestInfo(
                    entity_id="number.eve_degree_aa11_elevation",
                    unique_id="homekit-AA00A0A00000-aid:1-sid:30-cid:33",
                    friendly_name="Eve Degree AA11 Elevation",
                    capabilities={
                        "max": 9000,
                        "min": -450,
                        "mode": NumberMode.AUTO,
                        "step": 1,
                    },
                    state="0",
                    entity_category=EntityCategory.CONFIG,
                ),
            ],
        ),
    )
