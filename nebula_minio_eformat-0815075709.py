from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "nebula_minio_eformat-0815075709",
}


dag = DAG(
    "nebula_minio_eformat-0815075709",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `nebula_minio_eformat.pipeline`.
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

op_5250f914_f6ef_479d_9251_7a6a37a78ab9 = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'nebula_minio_eformat' --cos-endpoint http://s3.apps.nebula.sl --cos-bucket openshift-ai-test --cos-directory 'nebula_minio_eformat-0815075709' --cos-dependencies-archive 'process_data-5250f914-f6ef-479d-9251-7a6a37a78ab9.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.apps.nebula.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "nebula_minio_eformat-{{ ts_nodash }}",
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
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_5250f914_f6ef_479d_9251_7a6a37a78ab9.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_c5fc72e7_fc4e_4dc1_9769_cb58367d30a4 = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'nebula_minio_eformat' --cos-endpoint http://s3.apps.nebula.sl --cos-bucket openshift-ai-test --cos-directory 'nebula_minio_eformat-0815075709' --cos-dependencies-archive 'model_gradient_boost-c5fc72e7-fc4e-4dc1-9769-cb58367d30a4.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.apps.nebula.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "nebula_minio_eformat-{{ ts_nodash }}",
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
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_c5fc72e7_fc4e_4dc1_9769_cb58367d30a4.image_pull_policy = "Always"

op_c5fc72e7_fc4e_4dc1_9769_cb58367d30a4 << op_5250f914_f6ef_479d_9251_7a6a37a78ab9


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_e35f21a4_20dc_4c7c_b4ee_c8871ea2b628 = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'nebula_minio_eformat' --cos-endpoint http://s3.apps.nebula.sl --cos-bucket openshift-ai-test --cos-directory 'nebula_minio_eformat-0815075709' --cos-dependencies-archive 'model_randomforest-e35f21a4-20dc-4c7c-b4ee-c8871ea2b628.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.apps.nebula.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "nebula_minio_eformat-{{ ts_nodash }}",
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
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_e35f21a4_20dc_4c7c_b4ee_c8871ea2b628.image_pull_policy = "Always"

op_e35f21a4_20dc_4c7c_b4ee_c8871ea2b628 << op_5250f914_f6ef_479d_9251_7a6a37a78ab9


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_3597627b_15a5_438e_bf9c_7830f9782683 = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="airflow-eformat",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'nebula_minio_eformat' --cos-endpoint http://s3.apps.nebula.sl --cos-bucket openshift-ai-test --cos-directory 'nebula_minio_eformat-0815075709' --cos-dependencies-archive 'compare_and_push-3597627b-15a5-438e-bf9c-7830f9782683.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.apps.nebula.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "nebula_minio_eformat-{{ ts_nodash }}",
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
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_3597627b_15a5_438e_bf9c_7830f9782683.image_pull_policy = "Always"

op_3597627b_15a5_438e_bf9c_7830f9782683 << op_c5fc72e7_fc4e_4dc1_9769_cb58367d30a4

op_3597627b_15a5_438e_bf9c_7830f9782683 << op_e35f21a4_20dc_4c7c_b4ee_c8871ea2b628
