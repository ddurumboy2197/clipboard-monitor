class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}

    def is_allowed(self, ip_address):
        current_time = int(time.time())
        if ip_address not in self.requests:
            self.requests[ip_address] = []

        self.requests[ip_address] = [t for t in self.requests[ip_address] if t >= current_time - self.time_window]

        if len(self.requests[ip_address]) < self.max_requests:
            self.requests[ip_address].append(current_time)
            return True
        else:
            return False

    def reset(self, ip_address):
        if ip_address in self.requests:
            self.requests[ip_address] = []

# Misol foydalanuvchi
limiter = RateLimiter(max_requests=5, time_window=60)  # 5 ta so'rov 1 daqiqa ichida

print(limiter.is_allowed("192.168.1.1"))  # True
print(limiter.is_allowed("192.168.1.1"))  # True
print(limiter.is_allowed("192.168.1.1"))  # True
print(limiter.is_allowed("192.168.1.1"))  # True
print(limiter.is_allowed("192.168.1.1"))  # True
print(limiter.is_allowed("192.168.1.1"))  # False

limiter.reset("192.168.1.1")
print(limiter.is_allowed("192.168.1.1"))  # True
