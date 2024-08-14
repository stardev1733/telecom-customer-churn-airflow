from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "testing-pipeline1-0814031729",
}


dag = DAG(
    "testing-pipeline1-0814031729",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Ensure that the secret named '    secret-s64u0g' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="    secret-s64u0g",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="    secret-s64u0g",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/process_data.ipynb

op_0cde302c_809d_424e_83fb_9610a436c06e = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'testing-pipeline1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'testing-pipeline1-0814031729' --cos-dependencies-archive 'process_data-0cde302c-809d-424e-83fb-9610a436c06e.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "testing-pipeline1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "    secret-s64u0g", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "    secret-s64u0g", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_0cde302c_809d_424e_83fb_9610a436c06e.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_704b539c_7419_4d36_8611_0b04eecb4862 = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'testing-pipeline1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'testing-pipeline1-0814031729' --cos-dependencies-archive 'model_gradient_boost-704b539c-7419-4d36-8611-0b04eecb4862.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "testing-pipeline1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "    secret-s64u0g", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "    secret-s64u0g", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_704b539c_7419_4d36_8611_0b04eecb4862.image_pull_policy = "Always"

op_704b539c_7419_4d36_8611_0b04eecb4862 << op_0cde302c_809d_424e_83fb_9610a436c06e


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_939ddb61_fdd2_4090_8e9d_7b369dc7efaa = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'testing-pipeline1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'testing-pipeline1-0814031729' --cos-dependencies-archive 'model_randomforest-939ddb61-fdd2-4090-8e9d-7b369dc7efaa.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "testing-pipeline1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "    secret-s64u0g", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "    secret-s64u0g", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_939ddb61_fdd2_4090_8e9d_7b369dc7efaa.image_pull_policy = "Always"

op_939ddb61_fdd2_4090_8e9d_7b369dc7efaa << op_0cde302c_809d_424e_83fb_9610a436c06e


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_9a76a80f_83e5_4fd4_a10b_21778731137f = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'testing-pipeline1' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'testing-pipeline1-0814031729' --cos-dependencies-archive 'compare_and_push-9a76a80f-83e5-4fd4-a10b-21778731137f.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "testing-pipeline1-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "    secret-s64u0g", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "    secret-s64u0g", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_9a76a80f_83e5_4fd4_a10b_21778731137f.image_pull_policy = "Always"

op_9a76a80f_83e5_4fd4_a10b_21778731137f << op_704b539c_7419_4d36_8611_0b04eecb4862

op_9a76a80f_83e5_4fd4_a10b_21778731137f << op_939ddb61_fdd2_4090_8e9d_7b369dc7efaa
