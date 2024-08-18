from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Airflow-Test-0818082541",
}


dag = DAG(
    "Airflow-Test-0818082541",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `Airflow-Test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Ensure that the secret named 'aws-connection-nebula-minio-bucket' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="aws-connection-nebula-minio-bucket",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="aws-connection-nebula-minio-bucket",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/process_data.ipynb

op_24a12e14_3221_419f_b2ee_2fda8a19f8b0 = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="default",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Test' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Test-0818082541' --cos-dependencies-archive 'process_data-24a12e14-3221-419f-b2ee-2fda8a19f8b0.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Test-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio-bucket",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_S3_BUCKET",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_BUCKET",
        ),
        Secret(
            "env",
            "AWS_S3_ENDPOINT",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_ENDPOINT",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
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

op_24a12e14_3221_419f_b2ee_2fda8a19f8b0.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_16cfc89f_50ae_487e_96ae_dfcc953fcae6 = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="default",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Test' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Test-0818082541' --cos-dependencies-archive 'model_gradient_boost-16cfc89f-50ae-487e-96ae-dfcc953fcae6.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Test-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio-bucket",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_S3_BUCKET",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_BUCKET",
        ),
        Secret(
            "env",
            "AWS_S3_ENDPOINT",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_ENDPOINT",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
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

op_16cfc89f_50ae_487e_96ae_dfcc953fcae6.image_pull_policy = "Always"

op_16cfc89f_50ae_487e_96ae_dfcc953fcae6 << op_24a12e14_3221_419f_b2ee_2fda8a19f8b0


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_de00125d_255f_4967_9151_50c731637bd2 = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="default",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Test' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Test-0818082541' --cos-dependencies-archive 'model_randomforest-de00125d-255f-4967-9151-50c731637bd2.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Test-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio-bucket",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_S3_BUCKET",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_BUCKET",
        ),
        Secret(
            "env",
            "AWS_S3_ENDPOINT",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_ENDPOINT",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
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

op_de00125d_255f_4967_9151_50c731637bd2.image_pull_policy = "Always"

op_de00125d_255f_4967_9151_50c731637bd2 << op_24a12e14_3221_419f_b2ee_2fda8a19f8b0


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_a3c24bc4_e0b8_49e8_8a2b_a6dd69c49a05 = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="default",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'Airflow-Test' --cos-endpoint https://s3.apps.nebula.sl --cos-bucket openshift-ai-customer-churn --cos-directory 'Airflow-Test-0818082541' --cos-dependencies-archive 'compare_and_push-a3c24bc4-e0b8-49e8-8a2b-a6dd69c49a05.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Airflow-Test-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
            "AWS_SECRET_ACCESS_KEY",
        ),
        Secret(
            "env",
            "AWS_ACCESS_KEY_ID",
            "aws-connection-nebula-minio-bucket",
            "AWS_ACCESS_KEY_ID",
        ),
        Secret(
            "env",
            "AWS_DEFAULT_REGION",
            "aws-connection-nebula-minio-bucket",
            "AWS_DEFAULT_REGION",
        ),
        Secret(
            "env",
            "AWS_S3_BUCKET",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_BUCKET",
        ),
        Secret(
            "env",
            "AWS_S3_ENDPOINT",
            "aws-connection-nebula-minio-bucket",
            "AWS_S3_ENDPOINT",
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "aws-connection-nebula-minio-bucket",
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

op_a3c24bc4_e0b8_49e8_8a2b_a6dd69c49a05.image_pull_policy = "Always"

op_a3c24bc4_e0b8_49e8_8a2b_a6dd69c49a05 << op_16cfc89f_50ae_487e_96ae_dfcc953fcae6

op_a3c24bc4_e0b8_49e8_8a2b_a6dd69c49a05 << op_de00125d_255f_4967_9151_50c731637bd2
