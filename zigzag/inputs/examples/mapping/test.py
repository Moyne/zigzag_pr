mapping = {
    "default": {
        "core_allocation": 1,
        "spatial_mapping": {'D1': ('K', 32), 'D2': ('C', 32)},
        "temporal_ordering": [('K', 2), ('OY', 56), ('OX', 56), ('C', 2), ('FY', 3), ('FX', 3)],
        "memory_operand_links": {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
}
