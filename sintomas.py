
def calc_bayes(prior_A, prob_B_dado_A, pro_B):
    return (prior_A * prob_B_dado_A) / pro_B



if __name__ =='__main__':
    prob_cancer = 1/ 100000
    print (prob_cancer)
    prob_sintoma_dado_cancer = 1
    print (prob_sintoma_dado_cancer)
    pro_sintoma_dado_no_cancer = 10/ 99999
    print(pro_sintoma_dado_no_cancer)
    pro_no_cancer = 1 - prob_cancer
    print (pro_no_cancer)

    pro_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (pro_sintoma_dado_no_cancer * pro_no_cancer)
    print(pro_sintoma)
    prob_cancer_dado_sintoma = calc_bayes(prob_cancer,prob_sintoma_dado_cancer,pro_sintoma)

    print (prob_cancer_dado_sintoma)    