from __future__ import annotations
from austin_heller_repo.kafka_manager import KafkaManager
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict


class GameMaintenanceManager():

	def __init__(self, *, kafka_manager: KafkaManager):

		self.__kafka_manager = kafka_manager

	def start_maintenance(self):

		# TODO send KafkaMessage containing maintenance started details to main topic

		raise NotImplementedError()

	def stop_maintenance(self):

		# TODO send KafkaMessage containing maintenance stopped details to main topic

		raise NotImplementedError()


class GameMaintenanceManagerFactory():

	def __init__(self, *, kafka_manager: KafkaManager):
		self.__kafka_manager = kafka_manager

	def get_game_maintenance_manager(self) -> GameMaintenanceManager:

		return GameMaintenanceManager(
			kafka_manager=self.__kafka_manager
		)
