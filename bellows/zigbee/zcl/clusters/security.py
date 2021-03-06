"""Security and Safety Functional Domain"""

import bellows.types as t
from bellows.zigbee.zcl import Cluster


class IasZone(Cluster):
    cluster_id = 0x0500
    name = 'IAS Zone'
    ep_attribute = 'ias_zone'
    attributes = {
        # Zone Information
        0x0000: ('zone_state', t.uint8_t),  # enum8
        0x0001: ('zone_type', t.uint16_t),  # enum16
        0x0002: ('zone_status', t.uint16_t),  # bitmap16
        # Zone Settings
        0x0010: ('cie_addr', t.EmberEUI64),
        0x0011: ('zone_id', t.uint8_t),
        0x0012: ('num_zone_sensitivity_levels_supported', t.uint8_t),
        0x0013: ('current_zone_sensitivity_level', t.uint8_t),
    }
    server_commands = {
        0x0000: ('enroll_response', (t.uint8_t, t.uint8_t), True),
        0x0001: ('init_normal_op_mode', (), False),
        0x0002: ('init_test_mode', (), False),
    }
    client_commands = {
        0x0000: ('status_change_notification', (t.uint16_t, t.uint8_t, t.uint8_t, t.uint16_t), False),
        0x0001: ('enroll', (), False),
    }


class IasAce(Cluster):
    cluster_id = 0x0501
    name = 'IAS Ancillary Control Equipment'
    ep_attribute = 'ias_ace'
    attributes = {}
    server_commands = {
        0x0000: ('arm', (), False),
        0x0001: ('bypass', (), False),
        0x0002: ('emergency', (), False),
        0x0003: ('fire', (), False),
        0x0004: ('panic', (), False),
        0x0005: ('get_zone_id_map', (), False),
        0x0006: ('get_zone_info', (), False),
        0x0007: ('get_panel_status', (), False),
        0x0008: ('get_bypassed_zone_list', (), False),
        0x0009: ('get_zone_status', (), False),
    }
    client_commands = {
        0x0000: ('arm_response', (), True),
        0x0001: ('get_zone_id_map_response', (), True),
        0x0002: ('get_zone_info_response', (), True),
        0x0003: ('zone_status_changed', (), False),
        0x0004: ('panel_status_changed', (), False),
        0x0005: ('panel_status_response', (), True),
        0x0006: ('set_bypassed_zone_list', (), False),
        0x0007: ('bypass_response', (), True),
        0x0008: ('get_zone_status_response', (), True),
    }


class IasWd(Cluster):
    cluster_id = 0x0502
    name = 'IAS Warning Device'
    ep_attribute = 'ias_wd'
    attributes = {
        0x0000: ('max_duration', t.uint16_t),
    }
    server_commands = {
        0x0000: ('start_warning', (), False),
        0x0001: ('squawk', (), False),
    }
    client_commands = {}
