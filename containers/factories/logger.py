import loguru

def specific_log(name: str):
    loguru.logger.add(
        f"logs/{name}.log",
        filter=lambda record: record["extra"].get("name") == name,
        level="TRACE",
        retention="3 days"
    )
    return loguru.logger.bind(name=name)