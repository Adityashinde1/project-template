from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    pass


@dataclass(frozen=True)
class DataValidationConfig:
    pass


@dataclass(frozen=True)
class DataTransformationConfig:
    pass


@dataclass(frozen=True)
class ModelTrainerConfig:
    pass


@dataclass(frozen=True)
class ModelPredictorConfig:
    pass


@dataclass(frozen=True)
class ModelPusherConfig:
    pass
