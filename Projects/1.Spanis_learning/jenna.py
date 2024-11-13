import matplotlib.pyplot as plt
import numpy as np

# Daireyi oluştur
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Şekli ve metni çiz
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, color='purple')  # Daire
ax.fill(x, y, color='lightblue', alpha=0.5)  # Dairenin içini doldur

# Metni ekle
ax.text(0, 0, "JENNA", fontsize=36, weight='bold', color='blue', ha='center', va='center')

# Eksenleri gizle
ax.axis('off')

# Resmi kaydet
plt.savefig('jenna_circle.png', bbox_inches='tight')
plt.show()
