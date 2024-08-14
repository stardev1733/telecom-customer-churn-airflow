from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "train_and_compare-0814032351",
}


dag = DAG(
    "train_and_compare-0814032351",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `under_arid_skies.pipeline`.
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

op_f97a91e7_e6df_4a63_834e_231f3ab570d9 = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'train_and_compare-0814032351' --cos-dependencies-archive 'process_data-f97a91e7-e6df-4a63-834e-231f3ab570d9.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare-{{ ts_nodash }}",
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

op_f97a91e7_e6df_4a63_834e_231f3ab570d9.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_4d4afb18_b582_4ae3_a61d_93040f90875a = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'train_and_compare-0814032351' --cos-dependencies-archive 'model_randomforest-4d4afb18-b582-4ae3-a61d-93040f90875a.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare-{{ ts_nodash }}",
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

op_4d4afb18_b582_4ae3_a61d_93040f90875a.image_pull_policy = "Always"

op_4d4afb18_b582_4ae3_a61d_93040f90875a << op_f97a91e7_e6df_4a63_834e_231f3ab570d9


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_b6cf67e4_f0d5_4d72_ae39_1c41412db02b = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'train_and_compare-0814032351' --cos-dependencies-archive 'model_gradient_boost-b6cf67e4-f0d5-4d72-ae39-1c41412db02b.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare-{{ ts_nodash }}",
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

op_b6cf67e4_f0d5_4d72_ae39_1c41412db02b.image_pull_policy = "Always"

op_b6cf67e4_f0d5_4d72_ae39_1c41412db02b << op_f97a91e7_e6df_4a63_834e_231f3ab570d9


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_c39df858_5a53_422f_8a83_b41d15b4cd95 = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare' --cos-endpoint https://s3.apps.vedrats.sl --cos-bucket openshift-ai-test --cos-directory 'train_and_compare-0814032351' --cos-dependencies-archive 'compare_and_push-c39df858-5a53-422f-8a83-b41d15b4cd95.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "AWS_S3_ENDPOINT": "https://s3.apps.vedrats.sl",
        "AWS_S3_BUCKET": "openshift-ai-test",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare-{{ ts_nodash }}",
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

op_c39df858_5a53_422f_8a83_b41d15b4cd95.image_pull_policy = "Always"

op_c39df858_5a53_422f_8a83_b41d15b4cd95 << op_4d4afb18_b582_4ae3_a61d_93040f90875a

op_c39df858_5a53_422f_8a83_b41d15b4cd95 << op_b6cf67e4_f0d5_4d72_ae39_1c41412db02b
