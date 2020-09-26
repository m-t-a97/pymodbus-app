import abc

class ModbusDao(abc.ABC):
  @abc.abstractmethod
  def write_single_coil(self, address, value):
    pass

  @abc.abstractmethod
  def write_multiple_coils(self, address, value):
	  pass

  @abc.abstractmethod
  def write_single_register(self, address, value):
	  pass

  @abc.abstractmethod
  def write_multiple_registers(self, address, value):
	  pass

  @abc.abstractmethod
  def read_coils(self, address, value):
	  pass

  @abc.abstractmethod
  def read_discrete_inputs(self, address, value):
	  pass

  @abc.abstractmethod
  def read_input_registers(self, address, value):
	  pass

  @abc.abstractmethod
  def read_holding_registers(self, address, value):
	  pass


