# This class holds the flags to enable/disable printing values in main function of simulator
class Verbose:
    LTE_BS_info = 0
    Wifi_BS_info = 0

    profile_and_probability = 0
    LTE_user_data_rates = 0
    Wifi_user_data_rates = 0
    
    LTE_user_SINR_MCS_value = 0 
    Wifi_user_SNR_MCS_value = 0 
    
    LTE_user_req_PRB = 0 # use with printing 
    Wifi_user_req_slots = 0 # use with printing SNR MCS

    LTE_BS_Req_by_user = 0
    Wifi_BS_Req_by_user = 0

    CSMA_CA_Logs = 0
    LTE_proportions = 0

    vary_factor = 0

    frame_dictionary = 0

    state_action_Qtable = 0
    Qtable = 0


    plot_Scene = 0 # plotting graph of positioning of BS and UE in the scene
    plot_SINR_Count = 0 # plot number of LTE users vs SINR
    plot_SNR_Count = 0 # plot number of Wifi users vs SNR

    # end
    Table_Fairness_LTH_WTH = 0
    List_line_Fairness = 0  # prints long list of fairness values of each iteration
    List_line_LTE_throughput = 0  # prints long list of LTE throughput values of each iteration
    List_line_Wifi_throughput = 0  # prints long list of LTE throughput values of each iteration

    FairnessVsFrameIters = 0
