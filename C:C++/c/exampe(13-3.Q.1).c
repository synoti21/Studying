//
//  main.c
//  c
//
//  Created by 안지완 on 2021/09/19.
//

#include <stdio.h>

int sort_by_avg(int (*parr)[4],int row,int *arr_avg);


int main(){
    int test_result[5][4];
    int i,j;
    int each_sum = 0;
    int total_avg = 0;
    int *p_total_avg;
    
    p_total_avg = &total_avg;
    
    
    for (i = 0 ; i < 5; i++){
        for(j =0 ; j < 3; j++){
            scanf("%d",&test_result[i][j]);
        }
    }
    
    sort_by_avg(test_result,5,p_total_avg);
    
    for(i =0 ; i<5; i++){
        each_sum=0;
        for(j= 0 ; j<3; j++){
            printf("%d ",test_result[i][j]);
            each_sum += test_result[i][j];
        }
        printf("평균 : %d ",each_sum/3);
        if(each_sum >= total_avg){
            printf("합격");
        }else{
            printf("불합격");
        }
        printf("\n");
    }
    
    printf("전체 평균 : %d\n",total_avg/3);
    return 0;
}

int sort_by_avg(int (*parr)[4], int row, int *arr_avg){ //sorts test score array by average & gets total average
    
    int each_avg;
    int total_avg=0;
    int i,j,k;
    int temp[4];
    
    for(i = 0 ; i < row; i++){
        each_avg=0;
        for(j= 0; j < 3;j++){
            each_avg+=parr[i][j];
        }
        total_avg+=each_avg;
        parr[i][3] = each_avg;
    } //gets total average and puts value(average) to 4th element of each array
    
    for(i = 0 ; i < row-1 ; i++){
        for(j= i+1 ; j < row ; j ++){
            if(parr[j][3] > parr[i][3]){
                for(k = 0 ; k < 4; k++){
                    temp[k] = parr[i][k];
                    parr[i][k] = parr[j][k];
                    parr[j][k] = temp[k]; //change each element one by one (cannot swap entirely with pointer)
                }
            }
        }
    } //sort by average from highest to lowest
    
    *arr_avg = (total_avg)/row;
    return 0;
    
}


