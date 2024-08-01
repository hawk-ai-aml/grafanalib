"""Helpers to create Prometheus-specific Grafana queries."""
import attr

from grafanalib.core import Target, DEFAULT_STEP
from grafanalib.influxdb import TIME_SERIES_TARGET_FORMAT
from attr.validators import instance_of


@attr.s
class PrometheusTarget(Target):
    """
    Metric to show.

    :param target: Graphite way to select data
    """

    expr = attr.ib(default="")
    format = attr.ib(default=TIME_SERIES_TARGET_FORMAT)
    hide = attr.ib(default=False, validator=instance_of(bool))
    legendFormat = attr.ib(default="")
    interval = attr.ib(default="", validator=instance_of(str))
    intervalFactor = attr.ib(default=2)
    metric = attr.ib(default="")
    refId = attr.ib(default="")
    step = attr.ib(default=DEFAULT_STEP)
    target = attr.ib(default="")
    instant = attr.ib(validator=instance_of(bool), default=False)
    datasource = attr.ib(default=None)

    def to_json_data(self):
        return {
            'expr': self.expr,
            'target': self.target,
            'format': self.format,
            'hide': self.hide,
            'interval': self.interval,
            'intervalFactor': self.intervalFactor,
            'legendFormat': self.legendFormat,
            'metric': self.metric,
            'refId': self.refId,
            'step': self.step,
            'instant': self.instant,
            'datasource': self.datasource,
        }
