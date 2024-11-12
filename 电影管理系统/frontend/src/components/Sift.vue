<script setup>
import { movieStore } from '../apis/movies';
import {onMounted, computed } from 'vue';


const useMovieStore = movieStore();
const yearDate = new Date().getFullYear()
const numYears = 16
function createYearArray(yearDate,numYears) {
    let years = [];
    for (let i = 0; i < numYears; i++) {
        if(i==0){
            years.push({'id':i+1,
                'year' : '全部'
            })
        }
        if(i<10&&i>0) {
        years.push({'id':i+1,
                'year' : yearDate -i+1
            })

        }
        if(i==9) {
        years.push({'id':i+2,
                'year' : '2015-2010'
            })

        }
        if(i==10) {
        years.push({'id':i+2,
                'year' : '2009-2005'
            })

        }
        if(i==11) {
        years.push({'id':i+2,
                'year' : '2004-2000'
            })

        }
        if(i==12) {
        years.push({'id':i+2,
                'year' : '90年代'
            })
        }
        if(i==13) {
        years.push({'id':i+2,
                'year' : '80年代'
            })
        }
        if(i==14){
        years.push({'id':numYears,
                'year' : '更早'
            })
        }

    }
    return years;
}
const years = createYearArray(yearDate,numYears)
function SearchByYear(year) {
    if(year.year =='全部'){ useMovieStore.loadMovie()
    }
    else useMovieStore.getMovieByYear(year.year);
    document.querySelector('.on').classList.remove('on')
    document.querySelector(`li:nth-child(${year.id}).yearItem`).classList.add('on')
}

</script>

<template>
     <div class="sift">
                 <div class="sift-title">
                         筛选
                 </div>
                <div class="sift_condition">
                    <div class="sift-block">
                         <div class="sift-name">年份</div>
                         <div class="year">
                            <li :class="year.id==1 ? 'yearItem on' : 'yearItem'"  @click="SearchByYear(year)" v-for="year in years" :key="year.id">
                                {{ year.year }}
                            </li>
                         </div>
                    </div>
                </div>
            </div>
</template>

<style>
.sift {
    min-width: 260px;
    max-width: 260px;
}
.sift-title {
    font-size:18px;
    height: 44px;
}
.sift-block {
    display: flex;
}
.sift-name {
    min-width: 24px;
    height: 30px;
    color: #99a2aa;
    margin-right: 20px;
}
.year,.sift-name ,.yearItem{
    display: inline-block;
    font-size: 12px;
    cursor: pointer;
}
.yearItem {
    width: 50px;
    padding-right: 2px;
    height: 30px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.on {
    color: #00a1d6;
}
</style>