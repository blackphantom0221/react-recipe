"""empty message

Revision ID: 341c4625cbfe
Revises: 468e713d1b0b
Create Date: 2021-07-02 18:12:43.166059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '341c4625cbfe'
down_revision = '468e713d1b0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measurements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_ingredients',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('measurement_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['measurement_id'], ['measurements.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('ingredient_id', 'recipe_id')
    )
    op.drop_table('recipe_ingredient')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe_ingredient',
    sa.Column('ingredient_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('recipe_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], name='recipe_ingredient_ingredient_id_fkey'),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], name='recipe_ingredient_recipe_id_fkey'),
    sa.PrimaryKeyConstraint('ingredient_id', 'recipe_id', name='recipe_ingredient_pkey')
    )
    op.drop_table('recipe_ingredients')
    op.drop_table('measurements')
    # ### end Alembic commands ###
