from aws_cdk import (
    core,
    aws_backup as bk,
    aws_events as event
)

class CdkAwsBackupStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, env, **kwargs) -> None:
        super().__init__(scope, id, env=env, **kwargs)

        core_tag = core.Tags.of(self)

        # The code that defines your stack goes here
        backup_plan = bk.BackupPlan(
            scope=self,
            id="TestBackupCDK",
            backup_plan_name=f"test-backup-cdk"
        )

        backup_vault_name = f'test-backup-cdk-vault'
        bk_vault = bk.BackupVault(
            scope=self,
            id=f'testbackupcdkvault',
            backup_vault_name=backup_vault_name,
        )

        backup_plan.add_rule(
            rule=bk.BackupPlanRule(
                backup_vault=bk_vault,
                rule_name='backup-daily',
                delete_after=core.Duration.days(1),
                schedule_expression=event.Schedule.cron(
                    minute="0",
                    hour="0",
                    month="*",
                    week_day="*",
                    year="*"
                )
            )
        )

        backup_plan.add_selection(
            id=f'test-backup-cdk-selection',
            backup_selection_name=f"test-backup-cdk",
            resources=[
                bk.BackupResource.from_tag(
                    key='BackupID',
                    value='dailybackup'
                )
            ]
        )

        core_tag.add(
            key='cfn.aws-backup.stack',
            value='test'
        )
