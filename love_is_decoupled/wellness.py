from enum import Enum


class Wellness(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"