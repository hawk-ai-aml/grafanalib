import grafanalib.prometheus_target as C


def test_prometheus_target():
    """Test Cloudwatch Logs Insights target"""
    prometheus_expression = 'kube_job_status_failed{namespace="default",job_name=~"old-indices-removal.*"}'
    legend_format = '{{ job_name }} - failed'
    ref_id = "A"

    target = C.PrometheusTarget(
        expr=prometheus_expression,
        legendFormat=legend_format,
        refId=ref_id
    )

    data = target.to_json_data()

    assert data["expr"] == prometheus_expression
    assert data["refId"] == ref_id
    assert data["step"] == 1
    assert data["legendFormat"] == legend_format
