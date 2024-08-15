from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "eformat_testing_1-0815030618",
}


dag = DAG(
    "eformat_testing_1-0815030618",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `eformat_testing.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Ensure that the secret named 'aws-connection-vedrats-minio' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="aws-connection-vedrats-minio",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="aws-connection-vedrats-minio",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/process_data.ipynb

op_60fe19fb_09ec_4f15_9dcb_b7b49374c81e = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eformat_testing_1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'eformat_testing_1-0815030618' --cos-dependencies-archive 'process_data-60fe19fb-09ec-4f15-9dcb-b7b49374c81e.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eformat_testing_1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-vedrats-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-vedrats-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_60fe19fb_09ec_4f15_9dcb_b7b49374c81e.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_e7b211e7_6cd4_4c1d_a290_a9f78c49b9f9 = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eformat_testing_1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'eformat_testing_1-0815030618' --cos-dependencies-archive 'model_gradient_boost-e7b211e7-6cd4-4c1d-a290-a9f78c49b9f9.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eformat_testing_1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-vedrats-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-vedrats-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_e7b211e7_6cd4_4c1d_a290_a9f78c49b9f9.image_pull_policy = "Always"

op_e7b211e7_6cd4_4c1d_a290_a9f78c49b9f9 << op_60fe19fb_09ec_4f15_9dcb_b7b49374c81e


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_0bbe5a8c_f359_4d8e_81f4_3150ab1d108b = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eformat_testing_1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'eformat_testing_1-0815030618' --cos-dependencies-archive 'model_randomforest-0bbe5a8c-f359-4d8e-81f4-3150ab1d108b.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eformat_testing_1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-vedrats-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-vedrats-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_0bbe5a8c_f359_4d8e_81f4_3150ab1d108b.image_pull_policy = "Always"

op_0bbe5a8c_f359_4d8e_81f4_3150ab1d108b << op_60fe19fb_09ec_4f15_9dcb_b7b49374c81e


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_1026e951_a160_48e8_b7d3_b95b72c69a50 = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eformat_testing_1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'eformat_testing_1-0815030618' --cos-dependencies-archive 'compare_and_push-1026e951-a160-48e8-b7d3-b95b72c69a50.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eformat_testing_1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-vedrats-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-vedrats-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_1026e951_a160_48e8_b7d3_b95b72c69a50.image_pull_policy = "Always"

op_1026e951_a160_48e8_b7d3_b95b72c69a50 << op_e7b211e7_6cd4_4c1d_a290_a9f78c49b9f9

op_1026e951_a160_48e8_b7d3_b95b72c69a50 << op_0bbe5a8c_f359_4d8e_81f4_3150ab1d108b
