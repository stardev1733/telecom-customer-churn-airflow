from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "mypipe-0815063133",
}


dag = DAG(
    "mypipe-0815063133",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `mypipe.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Ensure that the secret named ' secret-ykuiqs' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret=" secret-ykuiqs",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret=" secret-ykuiqs",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/process_data.ipynb

op_3b75847e_11d1_4901_abab_c913a6db9fe3 = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="airflow-helm",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mypipe' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'mypipe-0815063133' --cos-dependencies-archive 'process_data-3b75847e-11d1-4901-abab-c913a6db9fe3.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mypipe-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", " secret-ykuiqs", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", " secret-ykuiqs", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_3b75847e_11d1_4901_abab_c913a6db9fe3.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_d72f6ac1_d7d6_471c_abb4_523ba7fb2599 = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="airflow-helm",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mypipe' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'mypipe-0815063133' --cos-dependencies-archive 'model_gradient_boost-d72f6ac1-d7d6-471c-abb4-523ba7fb2599.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mypipe-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", " secret-ykuiqs", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", " secret-ykuiqs", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_d72f6ac1_d7d6_471c_abb4_523ba7fb2599.image_pull_policy = "Always"

op_d72f6ac1_d7d6_471c_abb4_523ba7fb2599 << op_3b75847e_11d1_4901_abab_c913a6db9fe3


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_50cdec73_ece6_42f1_8fdb_f631c635ec50 = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="airflow-helm",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mypipe' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'mypipe-0815063133' --cos-dependencies-archive 'model_randomforest-50cdec73-ece6-42f1-8fdb-f631c635ec50.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mypipe-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", " secret-ykuiqs", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", " secret-ykuiqs", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_50cdec73_ece6_42f1_8fdb_f631c635ec50.image_pull_policy = "Always"

op_50cdec73_ece6_42f1_8fdb_f631c635ec50 << op_3b75847e_11d1_4901_abab_c913a6db9fe3


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_7c0a0884_a9dc_4be0_b326_1bf48b7dab91 = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="airflow-helm",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mypipe' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'mypipe-0815063133' --cos-dependencies-archive 'compare_and_push-7c0a0884-a9dc-4be0-b326-1bf48b7dab91.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mypipe-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", " secret-ykuiqs", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", " secret-ykuiqs", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_7c0a0884_a9dc_4be0_b326_1bf48b7dab91.image_pull_policy = "Always"

op_7c0a0884_a9dc_4be0_b326_1bf48b7dab91 << op_d72f6ac1_d7d6_471c_abb4_523ba7fb2599

op_7c0a0884_a9dc_4be0_b326_1bf48b7dab91 << op_50cdec73_ece6_42f1_8fdb_f631c635ec50
