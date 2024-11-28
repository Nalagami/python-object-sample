import logging
from dataclasses import dataclass


# 値オブジェクトの定義
# frozen=True にすることで、イミュータブルなオブジェクトになる
@dataclass(frozen=True)
class Sample:
    name: str
    age: int

    def __post_init__(self):
        # バリデーション
        if self.age < 0:
            raise ValueError("age must be positive")
        if not self.name:
            raise ValueError("name must be non-empty")
        if len(self.name) > 15:
            raise ValueError("name must be less than 15 characters")


@dataclass(frozen=True)
class ValueObject:
    """
    バリデーションを追加した値オブジェクト
    バリデーションチェックで失敗したときにログを出力し、例外を投げる
    """
    value: str
    value2: int

    def __post_init__(self):
        self._validate()

    def _validate(self):
        errors = []
        if not self.value:
            errors.append("value is required")
        if self.value not in {"1", "2", "3"}:
            errors.append("value must be 1, 2 or 3")
        if not isinstance(self.value2, int):
            errors.append("value2 must be int")

        if errors:
            logging.error(
                "Validation error",
                extra={
                    "param": {"value": self.value, "value2": self.value2},
                    "errors": errors,
                },
            )
            raise ValueError
