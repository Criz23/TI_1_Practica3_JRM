std_motion_steps = 3.0

Levy_exponent1 = 1.0
Levy_exponent7 = 0.7

beta = 1

n_steps1 = Levy_2d_df_1.shape[0]
print(n_steps1)
n_steps7 = Levy_2d_df_7.shape[0]
print('***')
print(n_steps7)

aux_domain1 = np.linspace(std_motion_steps-5, std_motion_steps+5, n_steps1)
aux_domain7 = np.linspace(std_motion_steps-5, std_motion_steps+5, n_steps7)

Levy_pdf1 = np.array([levy_stable.pdf(i, alpha=Levy_exponent1, beta=beta, loc=std_motion_steps) for i in aux_domain1])
Levy_pdf7 = np.array([levy_stable.pdf(j, alpha=Levy_exponent7, beta=beta, loc=std_motion_steps) for j in aux_domain7])

def search_change(trayectory, index):
    m1 = (trayectory.y_pos[index] - trayectory.y_pos[index-1]) / (trayectory.x_pos[index] - trayectory.x_pos[index-1])
    #print(m1)
    m2 = (trayectory.y_pos[index+1] - trayectory.y_pos[index]) / (trayectory.x_pos[index+1] - trayectory.x_pos[index])
    #print(m2)
    if(m1 == m2):
        return True
    else:
        return False