"""Inventory models"""


from app.utils.validators import validate_integer


class Resource:
    """Base class for resources"""

    def __init__(self, name, manufacturer, total, allocated):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources

        Note:
            'allocated' cannot exceed 'total'
        """

        self._name = name
        self._manufacturer = manufacturer
        validate_integer('total', total, min_value=0)
        self._total = total
        validate_integer(
            'allocated', allocated, 0, total,
            custom_max_message="Allocated inventory cannot exceed total inventory"
        )
        self._allocated = allocated

    @property
    def name(self):
        """

        Returns:
            str: the resource name
        """
        return self._name

    @property
    def manufacturer(self):
        """

        Returns:
            str: the resource manufacturer
        """
        return self._manufacturer

    @property
    def total(self):
        """

        Returns:
            int: the total inventory count
        """
        return self._total

    @property
    def allocated(self):
        """

        Returns:
            int: number of resources in use
        """
        return self._allocated

    @property
    def category(self):
        """

        Returns:
            str:the resource category
        """
        return self.__class__.__name__.lower()

    @property
    def available(self):
        """

        Returns:
            int: number of resources available for use
        """
        return self.total - self.allocated

    def __str__(self):
        return f"Resource name: {self.name}"

    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer};" \
               f" total amount: {self.total}; allocated: {self.allocated}"

    def claim(self, amnt):
        """
        Claim amnt of inventory items(if available)

        Args:
            amnt (int): Amount of inventory items to claim

        Returns:

        """
        validate_integer(
            'amnt', amnt, 1, self.available,
            custom_max_message="Cannot claim more than available"
        )
        self._allocated += amnt

    def freeup(self, amnt):
        """
        Returns an inventory item to the available pool

        Args:
            amnt (int): Number of items to return (cannot exceed number in use)

        Returns:

        """
        validate_integer(
            'amnt', amnt, 1, self.allocated,
            custom_max_message="Cannot freeup more than allocated"
        )
        self._allocated -= amnt

    def died(self, amnt):
        """
        Number of items to deallocate and remove from the inventory pool
        altogether
        Args:
            amnt (int): Number of items that have died

        Returns:

        """
        validate_integer(
            'amnt', amnt, 1, self.allocated,
            custom_max_message="Cannot retire more than allocated"
        )
        self._allocated -= amnt
        self._total -= amnt

    def purchased(self, amnt):
        """
        Add new inventory to the pool

        Args:
            amnt (int): Number of items to add to the pool

        Returns:

        """
        validate_integer('amnt', amnt, 1)
        self._total += amnt


class CPU(Resource):
    """Resource subclass used to track specific CPU inventory pools"""

    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            cores (int): number of cores
            socket (str): CPU socket type
            power_watts (int): CPU rated wattage
        """
        super().__init__(name, manufacturer, total, allocated)
        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer};" \
               f" total amount: {self.total}; allocated: {self.allocated}" \
               f" cores amount: {self.cores}; socket: {self.socket}; power: {self.power_watts} Watts."

    @property
    def cores(self):
        """
        Number of cores.

        Returns:
            int
        """
        return self._cores

    @property
    def socket(self):
        """
        The socket type for this CPU

        Returns:
            str
        """
        return self._socket

    @property
    def power_watts(self):
        """
        The rated wattage of this CPU

        Returns:
            int
        """
        return self._power_watts


class Storage(Resource):
    """
    A base class for storage devices - probably not used directly
    """

    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
        """
        super().__init__(name, manufacturer, total, allocated)
        validate_integer('capacity_gb', capacity_gb, 1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        """
        Indicated the capacity (in GB) of the storage device

        Returns:
            int
        """
        return self._capacity_gb

    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer}; category: {self.category}" \
               f" total amount: {self.total}; allocated: {self.allocated}; capacity: {self.capacity_gb} GB."


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, size, rpm):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
            size (str): indicates the device size (must be either 2.5" or 3.5")
            rpm (int): disk rotation speed (in rpm)
        """
        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        allowed_sizes = ['2.5"', '3.5"']
        if size not in allowed_sizes:
            raise ValueError(f'Invalid HDD size. Must be on of {",".join(allowed_sizes)}')
        validate_integer('rpm', rpm, 1_000, 50_000)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        """
        The HDD size (2.5" / 3.5")

        Returns:
            str
        """
        return self._size

    @property
    def rpm(self):
        """
        The HDD spin speed (rpm)

        Returns:
            int
        """
        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f"{s} size: {self.size}; RPM: {self.rpm}."


class SSD(Storage):
    """
    Class used for SSD type resources
    """
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, interface):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
            interface (str): indicates the device interface (e.g. PCIe NVMe 3.0 x4)
        """
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self.interface = interface

    def __repr__(self):
        s = super().__repr__()
        return f"{s} interface: {self.interface}."
