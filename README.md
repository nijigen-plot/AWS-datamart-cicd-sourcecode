# やりたいこと
AWSでデータマート用AthenaテーブルCICD

## 流れ
1. deployment/productionブランチへマージするとCodePipelineを介してCodeBuildで[buildspec.yml](https://github.com/nijigen-plot/AWS-datamart-cicd-sourcecode/blob/master/aws/buildspec.yml)が実行される
2. 必要なファイルをリリースしたうえで[CloudFormation](https://github.com/nijigen-plot/AWS-datamart-cicd-sourcecode/blob/master/aws/cloudformation/datamart-cicd.yml)のスタックが作成される
3. sqlファイルからクエリを読むLambda Function,それを実行するStepFunctionsステートマシン,ステートマシンを毎日定期実行するEventBridge Scheduler,これらの為のIAM Roleが作成される