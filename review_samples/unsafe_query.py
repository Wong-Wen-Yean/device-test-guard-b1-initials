def lookup_device(connection, device_id: str):
    # Deliberately unsafe: string formatting creates an injection risk.
    query = f"SELECT * FROM device_tests WHERE device_id = '{device_id}'"
    return connection.execute(query).fetchone()
