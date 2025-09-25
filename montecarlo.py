import numpy as np

# Stats
mu = 1137
sigma = 369

# Simulate 1000 months
usage = np.random.normal(mu, sigma, 1000)

# Assume pricing
flexi_price_per_gb = 2
fast1000_base = 2000
fast1000_extra_per_gb = 1

# Costs
flexi_cost = usage * flexi_price_per_gb
fast1000_cost = fast1000_base + np.maximum(usage-1000, 0) * fast1000_extra_per_gb

# Average cost
print("Average FLEXI Cost:", np.mean(flexi_cost))
print("Average FAST1000 Cost:", np.mean(fast1000_cost))
