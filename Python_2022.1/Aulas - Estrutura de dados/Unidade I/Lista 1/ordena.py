# void ordena_vet(int vet[], int tam){
#   int i, j, aux;
# for (j=0;j<tam;j++){
# 	for (i=0;i<tam;i++){
# 	if(vet[i]>vet[i+1]){
# 		aux=vet[i];
# 		vet[i]=vet[i+1];
# 		vet[i+1]=aux;
# 	}
# }
# }
# }

def ordena_vet(vetor, tam):
    for j in range(tam):
        for i in range(tam):
            if(vetor[i]>vetor[i+1]):
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux;
    return vetor


l = [2,0,3]
print(ordena_vet(l,2))