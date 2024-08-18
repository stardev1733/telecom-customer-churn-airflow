from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Airflow-Testing-1-0818091015",
}


dag = DAG(
    "Airflow-Testing-1-0818091015",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `Airflow-Testing-1.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Ensure that the secret named 'aws-connection-nebula-minio' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="aws-connection-nebula-minio",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="aws-connection-nebula-minio",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/process_data.ipynb

op_88b2b882_1830_4a1c_b000_7cf8717cb6d1 = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="telecom-customer-churn",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Testing-1' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Testing-1-0818091015' --cos-dependencies-archive 'process_data-88b2b882-1830-4a1c-b000-7cf8717cb6d1.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Testing-1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret("env", "AWS_S3_BUCKET", "aws-connection-nebula-minio", "AWS_S3_BUCKET"),
        Secret(
            "env", "AWS_S3_ENDPOINT", "aws-connection-nebula-minio", "AWS_S3_ENDPOINT"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
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

op_88b2b882_1830_4a1c_b000_7cf8717cb6d1.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_2110e1eb_b163_40cc_8079_0d0d2d5209a2 = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="telecom-customer-churn",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Testing-1' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Testing-1-0818091015' --cos-dependencies-archive 'model_randomforest-2110e1eb-b163-40cc-8079-0d0d2d5209a2.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Testing-1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret("env", "AWS_S3_BUCKET", "aws-connection-nebula-minio", "AWS_S3_BUCKET"),
        Secret(
            "env", "AWS_S3_ENDPOINT", "aws-connection-nebula-minio", "AWS_S3_ENDPOINT"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
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

op_2110e1eb_b163_40cc_8079_0d0d2d5209a2.image_pull_policy = "Always"

op_2110e1eb_b163_40cc_8079_0d0d2d5209a2 << op_88b2b882_1830_4a1c_b000_7cf8717cb6d1


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_0f4eb44c_1535_4509_b63d_94c2bf291be0 = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="telecom-customer-churn",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Testing-1' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Testing-1-0818091015' --cos-dependencies-archive 'model_gradient_boost-0f4eb44c-1535-4509-b63d-94c2bf291be0.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Testing-1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret("env", "AWS_S3_BUCKET", "aws-connection-nebula-minio", "AWS_S3_BUCKET"),
        Secret(
            "env", "AWS_S3_ENDPOINT", "aws-connection-nebula-minio", "AWS_S3_ENDPOINT"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
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

op_0f4eb44c_1535_4509_b63d_94c2bf291be0.image_pull_policy = "Always"

op_0f4eb44c_1535_4509_b63d_94c2bf291be0 << op_88b2b882_1830_4a1c_b000_7cf8717cb6d1


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_d56998f4_b37b_4203_a81f_44ae7709c1fa = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="telecom-customer-churn",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Testing-1' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Testing-1-0818091015' --cos-dependencies-archive 'compare_and_push-d56998f4-b37b-4203-a81f-44ae7709c1fa.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Testing-1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret("env", "AWS_S3_BUCKET", "aws-connection-nebula-minio", "AWS_S3_BUCKET"),
        Secret(
            "env", "AWS_S3_ENDPOINT", "aws-connection-nebula-minio", "AWS_S3_ENDPOINT"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio",
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

op_d56998f4_b37b_4203_a81f_44ae7709c1fa.image_pull_policy = "Always"

op_d56998f4_b37b_4203_a81f_44ae7709c1fa << op_2110e1eb_b163_40cc_8079_0d0d2d5209a2

op_d56998f4_b37b_4203_a81f_44ae7709c1fa << op_0f4eb44c_1535_4509_b63d_94c2bf291be0
